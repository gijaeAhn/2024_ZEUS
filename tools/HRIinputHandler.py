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



class HRIinputHandler:
    def __init__(self):
        self.audio_stream = sd.InputStream(samplerate = 44100, channels=1,dtype='float32', callback = self.micCallback)
        self.recording_buffer = []
        
        self.key_enable = True
        self.is_mic_open = False

        self.temp_wav_path = os.path.join(temp_file_path, "usr_voice.wav")
        self.temp_mp3_path = os.path.join(temp_file_path, 'usr_voice.mp3')
        
        self.keyboard = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.keyboard.start()
        self.enable_key()

        self.fsm_trigger = rospy.Publisher("hri_trigger", String, queue_size=1)

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

            if key_str == "z":
                print("trigger_z")
                self.fsm_trigger.publish("0")

            elif key_str == "x":
                self.closeMic()
                print("trigger_x")
                self.fsm_trigger.publish("1")

            elif key_str == "c":
                self.fsm_trigger.publish("2")
                 
        


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
        os.system(f"rm {os.path.join(home_dir, '.temp_files/*.mp3')}")
        os.system(f"ffmpeg -y -nostdin -i {self.temp_wav_path} {self.temp_mp3_path}")

    def enable_key(self):
        self.key_enable = True
        return


    def disable_key(self):
        self.key_enable = False
        return



if __name__ == "__main__":
    _ = HRIinputHandler()
    try:
         rospy.spin()
         print("success to activate HRIinputHandler node")
    except:
         exit()
