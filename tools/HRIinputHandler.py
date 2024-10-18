#!/home/sjlab3090/anaconda3/bin/python
import rospy
from std_msgs.msg import String

from pynput import keyboard
import sounddevice as sd
import os
import numpy as np
from scipy.io.wavfile import write


rospy.init_node("HRIinputHandler_Node")

home_dir = os.path.expanduser("~")
temp_file_path  = os.path.join(home_dir, ".temp_files")



class inputQueue:
    def __init__(self):
        self.is_full = False
        self.fsm_trigger = rospy.Publisher("hri_trigger", String, queue_size=1)
        self.hri_finish_listener = rospy.Subscriber('hri/loopfinish', String, callback=self.openQueue)
    
    def insert():
        pass

    def openQueue(self, msg):
        self.is_full = False
    
    def isFull(self,):
        return self.is_full
    
    def push(self, s):
        print(f"trigger_{s}")
        self.fsm_trigger.publish(s)
        self.is_full = True



class HRIinputHandler:
    def __init__(self):
        self.audio_stream = sd.InputStream(samplerate = 44100, channels=1,dtype='float32', callback = self.micCallback)
        self.recording_buffer = []
        
        self.key_enable = True
        self.is_mic_open = False

        self.temp_wav_path = os.path.join(temp_file_path, "usr_voice.wav")
        self.temp_mp3_path = os.path.join(temp_file_path, 'usr_voice.mp3')
        
        self.q = inputQueue()

        
        self.enable_key()

       
    def on_press(self, key):
            try :
                key_str = '{0}'.format(key.char)
            except :
                key_str = '{0}'.format(key)

            if key_str == 'x' and not self.is_mic_open:
                self.is_mic_open = not self.is_mic_open
                
                self.audio_stream.start()


    def on_release(self, key):

            
            try :
                key_str = '{0}'.format(key.char)
            except :
                key_str = '{0}'.format(key)
                
            if self.q.isFull():
                self.closeMic()
                return
            else:
                if key_str == "z":
                    print("trigger_z")
                    self.q.push("0")

                elif key_str == "x":
                    self.closeMic()
                    print("trigger_x")
                    self.q.push("1")

                elif key_str == "c":
                    self.q.push("2")
                 
    


    def micCallback(self, indata, frames, time, status):
        self.recording_buffer.append(indata.copy())
        # print(self.state)


    def closeMic(self):
        self.audio_stream.stop()
        print("audio stream closed")
        self.is_mic_open = not self.is_mic_open
        recorded_data_arr =  np.concatenate(self.recording_buffer, axis=0)

        write(self.temp_wav_path, 44100, recorded_data_arr)
        self.recording_buffer.clear()
        self.recording_buffer = []
        os.system(f"rm {os.path.join(home_dir, '.temp_files/*.mp3')}")
        os.system(f"ffmpeg -y -nostdin -i {self.temp_wav_path} {self.temp_mp3_path}")
        

    def enable_key(self):
        print("eneable key")
        self.keyboard = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.keyboard.start()
        return



if __name__ == "__main__":
    _ = HRIinputHandler()
    try:
         rospy.spin()
         print("success to activate HRIinputHandler node")
    except:
         exit()
