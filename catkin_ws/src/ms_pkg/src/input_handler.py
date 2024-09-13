import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))


import rospy
from ms_pkg.srv import LLMC_service, LLMC_serviceResponse
from ms_pkg.srv import STT_service, STT_serviceResponse
from ms_pkg.srv import TF_service, TF_serviceResponse
from ms_pkg.srv import FER_service, FER_serviceResponse

import os
import cv2
import sounddevice as sd
from scipy.io.wavfile import write
from pynput import keyboard
from cv_bridge import CvBridge
import numpy as np
import time

from custom_utils import EasyLogger as EL

node_name = "InputHandlerNode"
rospy.init_node(node_name)

config = {}
config["STT"] = rospy.get_param("~STT_SN", default="STTService")
config["LLMC"] = rospy.get_param("~LLMC_SN", default="LLMCService")
config["TF"] = rospy.get_param("~TF_SN", default="TFService")
config["FER"] = rospy.get_param("~FER_SN", default="FERService")
el = EL(node_name, config)
el.initHello()




temp_file_dir = os.path.expanduser(".temp_files")
sample_rate = 44100
duration = 5  # 5초 동안 녹음
bridge = CvBridge()


class InputHandler():
    def __init__(self, config = None):
        rospy.loginfo("Checking for service's activation")
        rospy.wait_for_service(config['STT'])
        rospy.wait_for_service(config['FER'])
        rospy.wait_for_service(config['LLMC'])
        rospy.wait_for_service(config['TF'])
        
        self.recording_buffer = []
        self.is_recording = False
        self.audio_steam = sd.InputStream(samplerate = sample_rate, channels=2, callback = self.callback)
        self.audio_save_path = os.path.join(temp_file_dir, "record.wav")
        
        self.STTService_rq = rospy.ServiceProxy(config["STT"], STT_service)
        self.TFService_rq = rospy.ServiceProxy(config["TF"], TF_service)
        self.FERService_rq = rospy.ServiceProxy(config["FER"], FER_service)
        self.LLMCservice_rq = rospy.ServiceProxy(config["LLMC"], LLMC_service)
        

        
    def callback(self, indata,  frames, time, status):
        if self.is_recording:
            self.recording_buffer.append(indata.copy())

    
    def startRecording(self, key):
        if not self.is_recording and key.char =='r':
            rospy.loginfo("오디오 스트림을 열겠습니다.")
            self.audio_steam.start() 
            self.is_recording = True
        
        if key == keyboard.Key.esc:    
            rospy.loginfo("프로그램을 종료합니다.")
            exit()
            

    def processInputHandlerLoop(self, key):
        if key.char == 'r':
            self.is_recording = False
            rospy.loginfo("오디오 스트림을 정지합니다")
            self.audio_steam.stop()

            if not len(self.recording_buffer):
                return 
            
            recorded_data_arr =  np.concatenate(self.recording_buffer, axis=0)
            write(self.audio_save_path, sample_rate, recorded_data_arr)
            self.recording_buffer.clear()
            stt_result = self.sendSTTRequest()
            rcmd_result = self.sendRecommandFilterRequese(stt_result)
            rospy.loginfo(stt_result)
            rospy.loginfo(rcmd_result)

            if rcmd_result:
                ret, frame = self.captureImagefromCam()
                if ret:
                    request_img = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
                    response = self.FERService_rq(request_img)
                    print(response.result)
                else:
                    rospy.loginfo("camera dosen't work")
            else:
                llm_answer = self.LLMCservice_rq(stt_result).model_text 
                print(llm_answer)


    def sendSTTRequest(self):
        stt_response = self.STTService_rq(self.audio_save_path).result
        return stt_response
    
    def sendRecommandFilterRequese(self, text):
        recommand_filter_response = self.TFService_rq(text).result
        return recommand_filter_response

    def captureImagefromCam(self):
        time.sleep(0.5)
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        return ret, frame

        



if __name__ == "__main__":
    voice_input = InputHandler(config=config)
    print("노무현은 살아있다")

    # 키보드 리스너 시작
    with keyboard.Listener(on_press=voice_input.startRecording, on_release=voice_input.processInputHandlerLoop) as listener:
        listener.join()





