import os, sys
home_dir = os.path.expanduser('~')
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module"))

import rospy
from std_msgs.msg   import String
from ms_pkg.srv import LLMC_service
from ms_pkg.srv import STT_service
from ms_pkg.srv import TF_service
from ms_pkg.srv import FER_service
from ms_pkg.srv import TTS_service

from ms_pkg.srv import IC_service
from ms_pkg.srv import Greeting_service

from config.config import WebotsConfig

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time
from gtts import gTTS
import time

# from pydub import AudioSegment

rospy.init_node("HRI_node")

config = {}
config["STT"] = rospy.get_param("~STT_SN", default="STTService")
config["LLMC"] = rospy.get_param("~LLMC_SN", default="LLMCService")
config["TF"] = rospy.get_param("~TF_SN", default="TFService")
config["FER"] = rospy.get_param("~FER_SN", default="FERService")
config["TTS"] = rospy.get_param("~TTS_SN", default="TTSService")



rospy.loginfo("Checking for service's activation")
rospy.wait_for_service(config['STT'])
rospy.wait_for_service(config['FER'])
rospy.wait_for_service(config['LLMC'])
rospy.wait_for_service(config['TF'])
rospy.wait_for_service(config['TTS'])
rospy.wait_for_service("ICService")
rospy.wait_for_service("GreetingService")
rospy.loginfo("All required Services are activated")

STTService_rq = rospy.ServiceProxy(config["STT"], STT_service)
TFService_rq = rospy.ServiceProxy(config["TF"], TF_service)
FERService_rq = rospy.ServiceProxy(config["FER"], FER_service)
LLMCservice_rq = rospy.ServiceProxy(config["LLMC"], LLMC_service)
TTSService_rq = rospy.ServiceProxy(config["TTS"], TTS_service)
ICService_rq = rospy.ServiceProxy("ICService", IC_service)
GreetingService_rq = rospy.ServiceProxy("GreetingService",Greeting_service)

gui_CommandPub = rospy.Publisher("gui_state_topic", String, queue_size=1)



def convert_wav_to_mp3(wav_path, mp3_path):
    print("im in convert_wav2mp3")
    os.system(f"rm {os.path.join(home_dir, '.temp_files/*.mp3')}")
    os.system(f"ffmpeg -y -nostdin -i {wav_path} {mp3_path}")
 

class Greeter:
    def __init__(self):
        self.greeting_signal_sub = rospy.Subscriber("greeting_signal", String, self.GreetingCallback)
        self.bye_signal_sub = rospy.Subscriber("bye_signal", String, self.GoodByeCallback) 

        self.history_load_pub = rospy.Publisher("chatbot_history_load_signal", String, queue_size=1)
        self.history_unload_pub = rospy.Publisher("chatbot_history_unload_siganl", String, queue_size=1)

    def GreetingCallback(self, _):
        #일단 가볍게 인사하고 사진찍기
        gui_CommandPub.publish("speaking")

        _ = TTSService_rq("어서오세요. 카메라를 봐주시겠어요?").result
        gui_CommandPub.publish("idle")
        
        time.sleep(0.5)
        cap_result = ICService_rq().result
        
        if cap_result:
            vision_answer = GreetingService_rq("inference", os.path.join(home_dir, ".temp_files/captured_img.png"), "사진을 보고 사진에 있는사람에게 자연스럽게 인사해줘").result
            print(vision_answer)
            
            gui_CommandPub.publish("speaking")
            _ = TTSService_rq(vision_answer).result
            gui_CommandPub.publish("idle")

            vision_model_history = GreetingService_rq("history", "", "").result
            self.history_load_pub.publish(vision_model_history)
            
            #chatbot should load upper vision model history

        else:
            return




    def GoodByeCallback(self, _):
        gui_CommandPub.publish("speaking")
        _ = TTSService_rq("안녕히가세요. 다음에 또 오세요").result
        gui_CommandPub.publish("idle")    
        self.history_unload_pub.publish("")





class HRI:
    def __init__(self):
        #file path variables
        self.menuList = WebotsConfig.menuList

        self.user_save_mp3 = os.path.expanduser("~/.temp_files/user_voice_command.mp3")
        self.user_save_wav = os.path.expanduser("~/.temp_files/user_voice_command.wav")
        self.user_answer_mp3 = os.path.expanduser("~/.temp_files/cheking_answer.mp3")
        self.user_answer_wav = os.path.expanduser("~/.temp_files/cheking_answer.wav")
        
        self.tts_save_path = os.path.expanduser("~/.temp_files/tts.mp3")


        self._HRICommandSub = rospy.Subscriber('HRICommand', String, self._HRICommandCallback)
        gui_CommandPub = rospy.Publisher("gui_state_topic", String, queue_size=1)


 

        self.orderPubblisher = rospy.Publisher("/zeus/webots/menu", String, queue_size=1)


        self.recording_buffer = []
        self.is_mic_open = False
        self.audio_stream = sd.InputStream(samplerate = 44100, channels=1,dtype='float32', callback = self._micCallback)
        self.last_action = "x"
       

    def _HRICommandCallback(self, msg): #누른 키에 따라서 대화처리 및 주문 처리
        print(msg.data, self.is_mic_open)
        key_str = msg.data
        if (key_str == "open" and not(self.is_mic_open)):
            gui_CommandPub.publish("listening")#<=Sending Signal to GUI Interface
            print("마이크를 활성화 합니다")
            print("녹음시작")
            
            self.is_mic_open = True
            self.last_action = key_str
            self.audio_stream.start()
            
        
        elif (key_str == 'x' or key_str == 'c') and self.is_mic_open:
            print("녹음끝")
            print("마이크를 비활성화 합니다")
            gui_CommandPub.publish("idle")#<=Sending Signal to GUI Interface
            self.is_mic_open = False
            self.audio_stream.stop()
            
            recorded_data_arr =  np.concatenate(self.recording_buffer, axis=0)
            write(self.user_save_wav, 44100, recorded_data_arr)
            convert_wav_to_mp3(self.user_save_wav, self.user_save_mp3)
            
            self.recording_buffer.clear()
            print("open event loop")
            
            if key_str == 'x':
                self._processVoiceInput()
            
            elif key_str == 'c':
               
                self._processOrderInput()
            print("close event loop")
            # self.audio_stream = sd.InputStream(samplerate = 44100, channels=1,dtype='float32', callback = self._micCallback)

            
    def _micCallback(self, indata, frames, time, status):
        self.recording_buffer.append(indata.copy())




    def _processVoiceInput(self):
        # import pdb; pdb.set_trace()
        stt_result = STTService_rq(self.user_save_mp3).result

        tf_result =  TFService_rq(stt_result, "recommand").result
        if tf_result:
            # fer_result = self.FERService_rq().result
            self._getMenuFromFace()
        else:
            llm_answer = LLMCservice_rq(stt_result).model_text
            gui_CommandPub.publish("speaking")
            tts_result = TTSService_rq(llm_answer).result
            gui_CommandPub.publish("idle")
            if not tts_result:
                print("tts failed")
                print(tts_result)
        

    
    
    def _processOrderInput(self):
        stt_result = STTService_rq(self.user_save_mp3).result
        tf_result =  TFService_rq(stt_result, "order").result

        if not tf_result:
            gui_CommandPub.publish("speaking")#<=Sending Signal to GUI Interface
            tts_result = TTSService_rq("죄송합니다. 말씀을 잘 못알아 듣겠습니다.").result
            gui_CommandPub.publish("idle")#<=Sending Signal to GUI Interface
            if not tts_result:
                print("tts failed")
                print(tts_result)
          
        else:
            user_answer = self._checkUsersAnswer(0, cheking_ment = f"말씀하신 메뉴가 {self.menuList[tf_result]}이 맞다면 '좋아' 아니면 '싫어'로 대답해 주세요.")
            gui_CommandPub.publish("speaking")#<=Sending Signal to GUI Interface
            if user_answer==1:
                
                _ = TTSService_rq(f"{self.menuList[tf_result]}를 제조하겠습니다.").result
                
                self.orderPubblisher.publish(self.menuList[tf_result])
                print("debug:" ,"success to send order to robot agent")
    
            elif user_answer ==-1:
                _ = TTSService_rq("싫으면 어쩔수 없지").result      
            
            elif user_answer ==-1:
                _ = TTSService_rq("어쩌하는거지?").result      
            gui_CommandPub.publish("idle")#<=Sending Signal to GUI Interface

    
    
    
    def _getMenuFromFace(self):
        gui_CommandPub.publish("speaking")#<=Sending Signal to GUI Interface
        guide_message = "네 메뉴를 추천해 드리겠습니다. 카메라를 봐주시겠어요?"
        # guide_message = "카메라 봐라"
        tts_result = TTSService_rq(guide_message).result
        gui_CommandPub.publish("idle")#<=Sending Signal to GUI Interface
        
        if not tts_result:
            print(tts_result)
        fer_score = FERService_rq().result
        
        if 0 <= fer_score < 0.33:
            recommand_menu = self.menuList[0]
            expression = "우울"
        
        elif 0.33 <= fer_score <0.66:
            recommand_menu = self.menuList[1]
            expression = "평범"
        
        else:
            recommand_menu = self.menuList[2]
            expression = "행복"
        gui_CommandPub.publish("speaking")#<=Sending Signal to GUI Interface

        recommand_ment = f"표정을 보아하니 기분이 {expression}해 보이시는군요, 이럴 때는 {recommand_menu}가 어울리죠!"
        # recommand_ment = "뻑"
        tts_result = TTSService_rq(recommand_ment).result
        
        if not tts_result:
            print("tts failed")
            print(tts_result)
        gui_CommandPub.publish("idle")#<=Sending Signal to GUI Interface
        
        user_answer = self._checkUsersAnswer(0, cheking_ment="추천하신 메뉴가 마음에 드시면 '좋아', 싫으면 '싫어'라고 대답해주세요.")
        print("user answer", user_answer)
        if user_answer ==1:
            robot_ment = f"{recommand_menu}를 제조하겠습니다"
            self.orderPubblisher.publish(recommand_menu) #<=== Agent에게 제조할 메뉴 보냄
        elif user_answer == 0:
            robot_ment = "'좋아' '싫어'로 대답하라고 좆간아"
        else:
            robot_ment = "싫으면 뭐 어쩔 수 없죠 ㅠㅠ"

        tts_result = TTSService_rq(robot_ment).result

        if not tts_result:
            print("tts failed")
            print(tts_result)
        return
        
    

    def _checkUsersAnswer(self, recurrent_stack, cheking_ment):
        # checking ment를 TTS로 말하고 응답이 negative인지 positive인지 여부를 최대 5회 까지 물어봄 positive:1, negative:-1, 확인불가:0 return 
        if recurrent_stack == 5:
            return 0
        gui_CommandPub.publish("speaking")#<=Sending Signal to GUI Interface
        
        tts_result = TTSService_rq(cheking_ment).result
        if not tts_result:
            print("tts failed")
            print(tts_result)
        gui_CommandPub.publish("listening")#<=Sending Signal to GUI Interface
        
        print("cheking user's answer")
        # time.sleep(0.1)
        audio_data = sd.rec(int(44100*2), samplerate=44100, channels=1, dtype='float32')
        sd.wait()
        write(self.user_answer_wav, 44100, audio_data)
        self.recording_buffer.clear()
        print("recording finished")
        convert_wav_to_mp3(self.user_answer_wav, self.user_answer_mp3)
        gui_CommandPub.publish("idle")#<=Sending Signal to GUI Interface
        
        stt_result = STTService_rq(self.user_answer_mp3).result
        print("user answer stt:", stt_result)
        cheking_result = TFService_rq(stt_result, "check_answer").result

        if cheking_result ==0:
            cheking_result = self._checkUsersAnswer(recurrent_stack+1, cheking_ment)

        return cheking_result


def main():
    hri = HRI()
    greeter = Greeter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutdown")

if __name__ == "__main__":
    main()
    
    
