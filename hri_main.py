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
subtitle_pub = rospy.Publisher("hri_subtitle", String, queue_size=1)
force_add_pub = rospy.Publisher("hri/force_order", String, queue_size=1)
order_pub = rospy.Publisher("/zeus/real/menu", String, queue_size=1)



menu_conversion_dict = {
    "모히또": "1",
    "모히토": "1", 
    '진토닉': "2", 
    '소맥': "3",
    '쏘맥':"3",
    '프랜치75': "4", 
    '프렌치75': "4",
    "마가리타": "5",
    "마티니": "6",

}

def hri_print(sub_msg, make_idle = True):
    gui.publish("speaking")
    subtitle_pub.publish("Cyber: "+ sub_msg)
    _ = TTSService_rq(sub_msg).result

    if make_idle:
        gui.publish("idle")

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

        
        self.hri_finish_pub = rospy.Publisher("hri/loopfinish", String, queue_size=1)
       

        self.order_ready = None
        self.mp3file_path = os.path.join(temp_file_path, "usr_voice.mp3")
        self.missing_stack = 0

        self.bridge = CvBridge()
 

    def act(self, msg):
        
        print("HRIMAIN::LOOP START")
        if msg.data == "miss":
            self.force_order()
            self.hri_finish_pub.publish("loop finished")
            return
        
        
        triggerd_data = int(msg.data)
        
        if self.state == "initial" and triggerd_data == 0:
            self.act_on_initial()

        elif self.state == "idle" and triggerd_data ==0: #고객이 떠나가는 상황
            self.act_on_goodbye()

        elif self.state == "idle" and triggerd_data == 1: #대화가 들어온 상황
            self.act_get_input()
            self.process_llm()

        elif self.state == "waiting_answer" and triggerd_data ==1:
            self.act_check_answer()

        elif self.state == "idle" and triggerd_data == 2:
            self.act_recommand_FER()

        
        self.hri_finish_pub.publish("loop finished")
        print("DEBUG::LOOP FINISH")

    
    def act_on_initial(self):
        
        hri_print("어서오세요. 카메라를 봐주시겠어요?", False)
        
        time.sleep(0.5)
        msg = rospy.wait_for_message('captured_img', Image, timeout=5)
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imwrite(HRIConfig.greeting_image_path, cv_image)
        
 
        greeting_ment = GreetingService_rq("inference").result
        
        hri_print(greeting_ment)
        
        gui.publish("idle")
        vision_model_history = GreetingService_rq("history").result
        self.history_load_pub.publish(vision_model_history)
        print("인사끝!")
        
        self.state = "idle"
    

    def act_on_goodbye(self):
        #clear models
        self.history_unload_pub.publish()
        hri_print("안녕히가세요. 다음에 또 오세요")
        subtitle_pub.publish() #clear subtitle label
        
        self.state = "initial"


    def act_get_input(self):
        gui.publish("listening")
        stt_result = STTService_rq(self.mp3file_path).result
        self.usr_text = stt_result
        subtitle_pub.publish("USER: " + stt_result)
        gui.publish("idle")


    def act_check_answer(self):
        force_add_pub.publish()
        stt_result = STTService_rq(self.mp3file_path).result
        context = detect_user_answer(stt_result)

        if context == 1:
            hri_print(f"네 {self.order_ready}를 제조하겠습니다.")
            order_pub.publish(menu_conversion_dict[self.order_ready])
            self.state = "idle"
            return

        elif context == 0:
            self.missing_stack = (self.missing_stack +1)%3 #3번 실패하면 다시 idle 상태로 
    
            if self.missing_stack%3 != 0:
                gui.publish("speaking")
                hri_print(f"죄송합니다. 답변을 잘 못알아들은것 같은데 '좋아', '싫어'로 다시 말씀해 주시겠어요?", make_idle=False)
                self.state = "waiting_answer"
                gui.publish("listening")
                
            else:
                hri_print(f"시스템에 에러가 있는것 같은데 다시 주문해주세요")
                self.state = "idle"
                return

        elif context == -1:
            hri_print(f"죄송합니다. 필요하신게 있으시면 다시 불러주세요.")
            self.state = "idle"
            return


    def process_llm(self):
        
        llm_answer = LLMCservice_rq(self.usr_text).result
        
        hri_print(llm_answer, False)
        
        situation, mentioned_menu  = detect_situation(llm_answer)


        # 메뉴 추천시
        if situation == 2:
            self.order_ready = mentioned_menu
            hri_print("추천한 메뉴가 마음에 드신다면 좋아, 싫으면 싫어라고 말씀해 주세요.", make_idle=False)
            self.state = "waiting_answer"
            gui.publish("listening")

            return

        # 메뉴 주문시
        elif situation == 1:
            self.order_ready = mentioned_menu
            hri_print(f"주문하신 메뉴가 {mentioned_menu}가 맞으면 맞아, 아니면 아니야 라고 말씀해 주세요.", make_idle=False)
            self.state = "waiting_answer"
            gui.publish("listening")
            return

        else:
            self.state = "idle"
            gui.publish("idle")
            return


    def act_recommand_FER(self):
        hri_print("네 메뉴를 추천해드리겠습니다. 카메라를 봐주시겠어요?", make_idle=False)

        msg = rospy.wait_for_message('captured_img', Image, timeout=5)
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imwrite(HRIConfig.fer_image_path, cv_image)

        print("###before send request")
        fer_result = FERService_rq().result
        print("###after send request")


        print("DUBUG::FERRESULT->",fer_result)
        if fer_result<0:
            hri_print("죄송하지만 카메라에 사람이 발견되지 않았습니다.", make_idle=True)
            self.state = "idle"
            return

        elif 0<=fer_result:
            if fer_result <0.33:
                self.order_ready = "진토닉"
                hri_print(f"표정을 보아하니 우울해 보이시는군요, 이럴 때는 {self.order_ready}를 추천해드립니다.", make_idle=False)
            elif 0.33 < fer_result < 0.66:
                self.order_ready = "마가리타"
                hri_print(f"표정을 보아하니 평범해 보이시는군요, 이럴 때는 {self.order_ready}를 추천해드립니다.", make_idle=False)
            elif 0.66 < fer_result:
                self.order_ready = "프렌치75"
                hri_print(f"표정을 보아하니 행복해 보이시는군요, 이럴 때는 {self.order_ready}를 추천해드립니다.", make_idle=False)
            

            hri_print("추천한 메뉴가 마음에 드신다면 좋아, 싫으면 싫어라고 말씀해 주세요.", make_idle=False)


            self.state = "waiting_answer"
            gui.publish("listening")
            return


    def force_order(self):
        hri_print("니는 씨발 주문할 생각이 없구나. 모히또나 쳐먹어라", make_idle=False)
        force_add_pub.publish()

if __name__ == "__main__":
    rospy.init_node("wtf")
    hri = HRI_FSM()
    # hri.enable_key()

    rospy.spin()






