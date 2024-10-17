#!/home/sjlab3090/anaconda3/bin/python
from pynput import keyboard
import time
import sounddevice as sd
import numpy as np
import cv2
import os
from scipy.io.wavfile import write

import rospy
from std_msgs.msg   import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ms_pkg.srv import LLMC_service
from ms_pkg.srv import STT_service
from ms_pkg.srv import TF_service
from ms_pkg.srv import FER_service
from ms_pkg.srv import TTS_service
from ms_pkg.srv import IC_service
from ms_pkg.srv import Greeting_service

from config.hri_config import HRIConfig


home_dir = os.path.expanduser("~")
temp_file_path  = os.path.join(home_dir, ".temp_files")


lg = rospy.loginfo

'''
there are some state like

no_custumer,
greeting,
goodbye
idle,
listening,


'''
config = {}
config["STT"] = rospy.get_param("~STT_SN", default="STTService")
config["LLMC"] = rospy.get_param("~LLMC_SN", default="LLMCService")
config["TF"] = rospy.get_param("~TF_SN", default="TFService")
config["FER"] = rospy.get_param("~FER_SN", default="FERService")
config["TTS"] = rospy.get_param("~TTS_SN", default="TTSService")

rospy.loginfo("Checking for service's activation")
# rospy.wait_for_service(config['STT'])
# rospy.wait_for_service(config['FER'])
# rospy.wait_for_service(config['LLMC'])
# rospy.wait_for_service(config['TF'])
# rospy.wait_for_service(config['TTS'])
# rospy.wait_for_service("ICService")
# rospy.wait_for_service("GreetingService")
rospy.loginfo("All required Services are activated")

STTService_rq = rospy.ServiceProxy(config["STT"], STT_service)
TFService_rq = rospy.ServiceProxy(config["TF"], TF_service)
FERService_rq = rospy.ServiceProxy(config["FER"], FER_service)
LLMCservice_rq = rospy.ServiceProxy(config["LLMC"], LLMC_service)
TTSService_rq = rospy.ServiceProxy(config["TTS"], TTS_service)
GreetingService_rq = rospy.ServiceProxy("GreetingService",Greeting_service)


gui = rospy.Publisher("gui_state_topic", String, queue_size=1)


def detect_situation(text):
    menu_flag = False 
    order_flag = False
    recommand_flag = False
    
    target_menu = None

    for w in HRIConfig.order_wordset:
        if w in text:
            order_flag =True
            break

    for w in HRIConfig.menu_wordset:
        if w in text:
            menu_flag = True
            target_menu = w
            break
    
    # for w in HRIConfig.recommand_wordset:
    #     if w in text:
    #         recommand_flag = True
    #         break


    # if menu_flag and recommand_flag:
    #     return 2, target_menu #매뉴 추천시 2를 반환
    
    if menu_flag and order_flag:
        return 1, target_menu #메뉴를 주문시 1을 반환

    else:
        return 0, target_menu


def detect_user_answer(text):
    for w in HRIConfig.positive_wordset:
        if w in text:
            return 1

    for w in HRIConfig.negative_wordset:
        if w in text:
            return -1
    
    return 0


class HRI_FSM:
    def __init__(self):
        self.state = "initial"
        self.trigger_listener = rospy.Subscriber("hri_trigger", String, self.act)

        self.usr_text = ""
        self.sys_text = ""

        self.history_load_pub = rospy.Publisher("chatbot_history_load_signal", String, queue_size=1)
        self.history_unload_pub = rospy.Publisher("chatbot_history_unload_siganl", String, queue_size=1)

        
        self.hri_finish_publisher = rospy.Publisher("hri/loopfinish", String, queue_size=1)

        self.order_ready = None
        self.mp3file_path = os.path.join(temp_file_path, "usr_voice.mp3")
        self.missing_stack = 0

        self.bridge = CvBridge()

    def act(self, msg):
        print("in act")
        triggerd_data = int(msg.data)
        
        if self.state == "initial" and triggerd_data == 0:
            self.act_on_initial()

        elif self.state == "idle" and triggerd_data ==0: #고객이 떠나가는 상황
            self.act_on_goodbye()

        elif self.state == "idle" and triggerd_data == 1:
            self.act_get_input()
            self.process_llm()

        elif self.state == "waiting_answer" and triggerd_data ==1:
            
            self.act_check_answer()

        elif self.state == "idle" and triggerd_data == 2:
            self.act_recommand_FER()
        
        self.hri_finish_publisher.publish()

    
    def act_on_initial(self):
        gui.publish("speaking")

        _ = TTSService_rq("어서오세요. 카메라를 봐주시겠어요?").result
        
        

        time.sleep(0.5)
        msg = rospy.wait_for_message('captured_img', Image, timeout=5)
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imwrite(HRIConfig.greeting_image_path, cv_image)
        
 
        
        vision_answer = GreetingService_rq("inference").result
        print(vision_answer)
        gui.publish("speaking")
    
        _ = TTSService_rq(vision_answer).result
        gui.publish("idle")
        vision_model_history = GreetingService_rq("history").result
        self.history_load_pub.publish(vision_model_history)
        print("인사했다 치고")
        # _ = TTSService_rq("인사했다 치고").result
        
        self.state = "idle"
    

    def act_on_goodbye(self):
        gui.publish("speaking")
        self.history_unload_pub.publish()
        _ = TTSService_rq("안녕히가세요").result
        gui.publish("idle")

        #clear models
        self.state = "initial"


    def act_get_input(self):
        stt_result = STTService_rq(self.mp3file_path).result
        self.usr_text = stt_result


    def act_check_answer(self):
        stt_result = STTService_rq(self.mp3file_path).result
        context = detect_user_answer(stt_result)

        if context == 1:
            gui.publish("speaking")
            _ = TTSService_rq(f"네 {self.order_ready}를 제조하겠습니다.")
            gui.publish('idle')
            self.state = "idle"
            return

        elif context == 0:
            self.missing_stack = (self.missing_stack +1)%3 #3번 실패하면 다시 idle 상태로 
    
            if self.missing_stack%3 != 0:
                gui.publish("speaking")
                _ = TTSService_rq(f"죄송합니다. 답변을 잘 못알아들은것 같은데 '좋아', '싫어'로 다시 말씀해 주시겠어요?")
                self.state = "waiting_answer"
                gui.publish("listening")
                
            else:
                gui.publish("speaking")
                _ = TTSService_rq(f"시스템에 에러가 있는것 같은데 다시 주문해주세요")
                self.order_ready = None
                self.state = "idle"
                gui.publish("idle")
            return

        elif context == -1:
            gui.publish("speaking")
            _ = TTSService_rq(f"죄송합니다. 필요하신게 있으시면 다시 불러주세요.")
            self.state = "idle"
            gui.publish("idle")
            return


    def process_llm(self):
        print("user_text:::", self.usr_text)
        llm_answer = LLMCservice_rq(self.usr_text).result
        print("im here")
        print(llm_answer)
        _ = TTSService_rq(llm_answer).result
        
        situation, mentioned_menu  = detect_situation(llm_answer)

        gui.publish("speaking")
        # 메뉴 추천시
        if situation == 2:
            self.order_ready = mentioned_menu
            _ = TTSService_rq("추천한 메뉴가 마음에 드신다면 좋아, 싫으면 싫어라고 말씀해 주세요.").result
            self.state = "waiting_answer"
            gui.publish("listening")
            return

        # 메뉴 주문시
        elif situation == 1:
            self.order_ready = mentioned_menu
            _ = TTSService_rq(f"주문하신 메뉴가 {mentioned_menu}가 맞으면 맞아, 아니면 아니야 라고 말씀해 주세요.").result
            self.state = "waiting_answer"
            gui.publish("listening")
            return

        else:
            self.state = "idle"
            gui.publish("idle")
            return


    def act_recommand_FER(self):
        gui.publish("speaking")
        _ =TTSService_rq("네 메뉴를 추천해드리겠습니다. 카메라를 봐주시겠어요?").result

        fer_result = FERService_rq().result
        print("ferresult:::",fer_result)
        if fer_result<0:
            _ =TTSService_rq("죄송하지만 카메라에 사람이 발견되지 않았습니다.").result
            self.state = "idle"
            return

        elif 0<=fer_result:
            if fer_result <0.33:
                self.order_ready = "진토닉"
                _ = TTSService_rq(f"표정을 보아하니 우울해 보이시는군요, 이럴 때는 {self.order_ready}를 추천해드립니다.")
            elif 0.33 < fer_result < 0.66:
                self.order_ready = "마가리타"
                _ = TTSService_rq(f"표정을 보아하니 평범해 보이시는군요, 이럴 때는 {self.order_ready}를 추천해드립니다.")
            elif 0.66 < fer_result:
                self.order_ready = "프렌치75"
                _ = TTSService_rq(f"표정을 보아하니 행복해 보이시는군요, 이럴 때는 {self.order_ready}를 추천해드립니다.")
            
            _ = TTSService_rq("추천한 메뉴가 마음에 드신다면 좋아, 싫으면 싫어라고 말씀해 주세요.").result

            self.state = "waiting_answer"
            print("herherer:::", self.state)
            gui.publish("listening")
            return


if __name__ == "__main__":
    rospy.init_node("wtf")
    hri = HRI_FSM()
    # hri.enable_key()

    rospy.spin()






