from positionLogger import positionLogger


from ms_pkg.srv import LLMC_service, LLMC_serviceResponse
from ms_pkg.srv import STT_service, STT_serviceResponse
from ms_pkg.srv import TF_service, TF_serviceResponse
from ms_pkg.srv import FER_service, FER_serviceResponse

import rospy
import cv2
import sounddevice as sd
from scipy.io.wavfile import write
from pynput import keyboard
from cv_bridge import CvBridge
import numpy as np
import time
import sys, os
sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module"))
# sys.path.append(os.path.expanduser("~/Desktop/2024_ZEUS/module/ms_library"))

from ms_library.custom_utils import EasyLogger as EL
from recommand_from_fer import recommand_from_fer
config = {}
config["STT"] = rospy.get_param("~STT_SN", default="STTService")
config["LLMC"] = rospy.get_param("~LLMC_SN", default="LLMCService")
config["TF"] = rospy.get_param("~TF_SN", default="TFService")
config["FER"] = rospy.get_param("~FER_SN", default="FERService")
# el = EL(node_name, config)

bridge = CvBridge()


def captureImagefromCam():
        time.sleep(0.5)
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        return ret, frame




class SysUserInterface(positionLogger):
    def __init__(self):
        super().__init__()
        rospy.loginfo("Checking for service's activation")
        rospy.wait_for_service(config['STT'])
        rospy.wait_for_service(config['FER'])
        rospy.wait_for_service(config['LLMC'])
        rospy.wait_for_service(config['TF'])
        
        self.recording_buffer = []
        self.is_stream_open = False
        self.audio_stream = sd.InputStream(samplerate = 44100, channels=2, callback = self.voice_callback)
        self.audio_save_dir = os.path.expanduser("~/.temp_files")
        os.makedirs(self.audio_save_dir, exist_ok=True)
        self.audio_save_path = os.path.join(os.path.expanduser("~/.temp_files"), "record.wav")
        
        self.STTService_rq = rospy.ServiceProxy(config["STT"], STT_service)
        self.TFService_rq = rospy.ServiceProxy(config["TF"], TF_service)
        self.FERService_rq = rospy.ServiceProxy(config["FER"], FER_service)
        self.LLMCservice_rq = rospy.ServiceProxy(config["LLMC"], LLMC_service)

    
    # @override
    def on_press(self, key):
        
        try :
            key_str = '{0}'.format(key.char)
        except :
            key_str = '{0}'.format(key)

        if key_str == 'r':
            
           self.toggle_audio_stream()
           if not self.is_stream_open:
                self.process_voice_input()
        else:
            self._moveCommandPub.publish(key_str)
    
    
    # @override
    def on_release(self, key):
        if key == keyboard.Key.esc:    
            rospy.loginfo("프로그램을 종료합니다.")
            return

    def voice_callback(self, indata,  frames, time, status):
        self.recording_buffer.append(indata.copy())

    def toggle_audio_stream(self):
        if self.is_stream_open == False:
            print("Open audio stream")
            self.is_stream_open = True
            self.audio_stream.start()
        else:
            self.is_stream_open = False
            print("close audio stream")
            self.audio_stream.stop()
            
            recorded_data_arr =  np.concatenate(self.recording_buffer, axis=0)
            write(self.audio_save_path, 44100, recorded_data_arr)
            self.recording_buffer.clear()
    
    def process_voice_input(self):
        stt_result = self.STTService_rq(self.audio_save_path).result
        tf_result =  self.TFService_rq(stt_result).result
        print(stt_result)
        if tf_result:
            ret, frame = captureImagefromCam()
            if ret:
                request_img = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
                fer_score = self.FERService_rq(request_img).result
                print(fer_score)
                print(type(fer_score))
                print("here")
                best_menu = recommand_from_fer(fer_score)
                print(best_menu)

            else:
                print("camera dosen't work")
        else:
            llm_answer = self.LLMCservice_rq(stt_result).model_text 
            print(llm_answer)


def main():
    sys_user_interface = SysUserInterface()
    # el.initHello()
    rospy.init_node("sys_user")
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutdown")


if __name__ == "__main__":

    main()