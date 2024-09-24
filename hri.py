import os, sys
home_dir = os.path.expanduser('~')
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module"))

import rospy
from std_msgs.msg   import String

from ms_pkg.srv import LLMC_service, LLMC_serviceResponse
from ms_pkg.srv import STT_service, STT_serviceResponse
from ms_pkg.srv import TF_service, TF_serviceResponse
from ms_pkg.srv import FER_service, FER_serviceResponse
from ms_pkg.srv import TTS_service, TTS_serviceResponse

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time
from gtts import gTTS
# from pydub import AudioSegment

rospy.init_node("HRI_node")

config = {}
config["STT"] = rospy.get_param("~STT_SN", default="STTService")
config["LLMC"] = rospy.get_param("~LLMC_SN", default="LLMCService")
config["TF"] = rospy.get_param("~TF_SN", default="TFService")
config["FER"] = rospy.get_param("~FER_SN", default="FERService")
config["TTS"] = rospy.get_param("~TTS_SN", default="TTSService")


def convert_wav_to_mp3(wav_path, mp3_path):
    print("im in convert_wav2mp3")
    os.system(f"rm {os.path.join(home_dir, '.temp_files/*.mp3')}")
    os.system(f"ffmpeg -y -nostdin -i {wav_path} {mp3_path}")
 

class HRI:
    def __init__(self):
        #file path variables
        self.user_save_mp3 = os.path.expanduser("~/.temp_files/user_voice_command.mp3")
        self.user_save_wav = os.path.expanduser("~/.temp_files/user_voice_command.wav")
        self.user_answer_mp3 = os.path.expanduser("~/.temp_files/cheking_answer.mp3")
        self.user_answer_wav = os.path.expanduser("~/.temp_files/cheking_answer.wav")
        
        self.tts_save_path = os.path.expanduser("~/.temp_files/tts.mp3")


        self._HRICommandSub = rospy.Subscriber('HRICommand', String, self._HRICommandCallback)

        rospy.loginfo("Checking for service's activation")
        rospy.wait_for_service(config['STT'])
        rospy.wait_for_service(config['FER'])
        rospy.wait_for_service(config['LLMC'])
        rospy.wait_for_service(config['TF'])
        rospy.wait_for_service(config['TTS'])
        rospy.loginfo("All required Services are activated")

        self.STTService_rq = rospy.ServiceProxy(config["STT"], STT_service)
        self.TFService_rq = rospy.ServiceProxy(config["TF"], TF_service)
        self.FERService_rq = rospy.ServiceProxy(config["FER"], FER_service)
        self.LLMCservice_rq = rospy.ServiceProxy(config["LLMC"], LLMC_service)
        self.TTSService_rq = rospy.ServiceProxy(config["TTS"], TTS_service)

        self.orderPubblisher = rospy.Publisher("/zeus/webots/menu", String, queue_size=1)


        self.recording_buffer = []
        self.is_mic_open = False
        self.audio_stream = sd.InputStream(samplerate = 44100, channels=1,dtype='float32', callback = self._micCallback)
       

    def _HRICommandCallback(self, msg):
        print(msg.data, self.is_mic_open)
        if msg.data == 'o' and not(self.is_mic_open):
            print("마이크를 활성화 합니다")
            print("녹음시작")
            
            self.is_mic_open = True
            self.audio_stream.start()
            
        
        elif msg.data == 'c' and self.is_mic_open:
            print("녹음끝")
            print("마이크를 비활성화 합니다")
            self.is_mic_open = False
            self.audio_stream.stop()
            
            recorded_data_arr =  np.concatenate(self.recording_buffer, axis=0)
            write(self.user_save_wav, 44100, recorded_data_arr)
            convert_wav_to_mp3(self.user_save_wav, self.user_save_mp3)
            print("here")
            self.recording_buffer.clear()
            print("open event loop")
            self._processVoiceInput()
            print("close event loop")
            # self.audio_stream = sd.InputStream(samplerate = 44100, channels=1,dtype='float32', callback = self._micCallback)

            
    def _micCallback(self, indata, frames, time, status):
        self.recording_buffer.append(indata.copy())


    def _processVoiceInput(self):
        # import pdb; pdb.set_trace()
        stt_result = self.STTService_rq(self.user_save_mp3).result

        tf_result =  self.TFService_rq(stt_result, "recommand").result
        if tf_result:
            # fer_result = self.FERService_rq().result
            self._getMenuFromFace()
        else:
            llm_answer = self.LLMCservice_rq(stt_result).model_text
            tts_result = self.TTSService_rq(llm_answer).result

            if not tts_result:
                print("tts failed")
                print(tts_result)
        

    def _getMenuFromFace(self):
        guide_message = "네 메뉴를 추천해 드리겠습니다. 카메라를 봐주시겠어요?"
        # guide_message = "카메라 봐라"
        tts_result = self.TTSService_rq(guide_message).result
        if not tts_result:
            print(tts_result)
        fer_score = self.FERService_rq().result
        
        if 0 <= fer_score < 0.33:
            recommand_menu = "마티니"
            expression = "우울"
        
        elif 0.33 <= fer_score <0.66:
            recommand_menu = "깔루아 밀크"
            expression = "평범"
        
        else:
            recommand_menu = "미도리 샤워"
            expression = "행복"

        recommand_ment = f"표정을 보아하니 기분이 {expression}해 보이시는군요, 이럴 때는 {recommand_menu}가 어울리죠!"
        # recommand_ment = "뻑"
        tts_result = self.TTSService_rq(recommand_ment).result
        if not tts_result:
            print("tts failed")
            print(tts_result)
        
        user_answer = self._checkUsersAnswer(0)
        print("user answer", user_answer)
        if user_answer ==1:
            robot_ment = f"{recommand_menu}를 제조하겠습니다"
            self.orderPubblisher.publish(recommand_menu) #<=== Agent에게 제조할 메뉴 보냄
        elif user_answer == 0:
            robot_ment = "'좋아' '싫어'로 대답하라고 좆간아"
        else:
            robot_ment = "싫으면 뭐 어쩔 수 없죠 ㅠㅠ"

        tts_result = self.TTSService_rq(robot_ment).result

        if not tts_result:
            print("tts failed")
            print(tts_result)
        return
        
    
    def _checkUsersAnswer(self, recurrent_stack):
        print(recurrent_stack)
        
        if recurrent_stack == 5:
            return 0
        
        cheking_ment = "추천하신 메뉴가 마음에 드시면 '좋아', 싫으면 '싫어'라고 대답해주세요."
        tts_result = self.TTSService_rq(cheking_ment).result
        if not tts_result:
            print("tts failed")
            print(tts_result)
        
        print("cheking user's answer")
        # time.sleep(0.1)
        audio_data = sd.rec(int(44100*2), samplerate=44100, channels=1, dtype='float32')
        sd.wait()
        write(self.user_answer_wav, 44100, audio_data)
        self.recording_buffer.clear()
        print("recording finished")
        convert_wav_to_mp3(self.user_answer_wav, self.user_answer_mp3)
        
        stt_result = self.STTService_rq(self.user_answer_mp3).result
        print("user answer stt:", stt_result)
        cheking_result = self.TFService_rq(stt_result, "check_answer").result

        if cheking_result ==0:
            cheking_result = self._checkUsersAnswer(recurrent_stack+1)

        return cheking_result



def main():
    hri = HRI()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutdown")

if __name__ == "__main__":
    main()
    
    
