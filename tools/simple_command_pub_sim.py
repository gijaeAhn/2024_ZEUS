
import sys
import os

home_dir = os.path.expanduser('~')

sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))

from utils.transformTotf import *

import rospy 

from pynput import keyboard

from lib.zeus_kinematics import *


from sensor_msgs.msg import JointState

from tf.msg import tfMessage
from std_msgs.msg   import String
from ms_pkg.srv import Greeting_service






class simple_command_pub_sim :

    def __init__(self):

        self.exist_user = False
        
        keyListener               =      keyboard.Listener(on_press= self.on_press, on_release= self.on_release)

        keyListener.start()

        self._savedTransform      =      None

        self._transSub            =      rospy.Subscriber("/zeus/webots/realTF", tfMessage, self._transSubCallback) 

        self._moveCommandPub      =      rospy.Publisher("/zeus/webots/simpleMoveCommand",String, queue_size= 10) #키 값을 받아서 WebotClient에게 넘겨주는 Publisher, 키가 눌릴때마다 그 값이 webotClient 에게 전달됨.

        self._HRICommandPub       =      rospy.Publisher("HRICommand", String, queue_size=1) #modified by ms

        self.GreetingPub          =     rospy.Publisher("greeting_signal", String, queue_size=1)
        
        self.ByePub               =     rospy.Publisher("bye_signal", String, queue_size=1)

        self.input_lock           =      False

    def on_press(self,key) :
            try :
                key_str = '{0}'.format(key.char)
            except :
                key_str = '{0}'.format(key)
            
            # "z" isuser exit state toggle button 
            if key_str == 'z':
                
                if self.exist_user == True:
                    self.ByePub.publish("")
                    print("user left our bar")

                else:
                    self.GreetingPub.publish("")
                    print("user came in our bar")

                self.exist_user = not self.exist_user
                return


            if self.exist_user: # 유저가 있는상태에서 
                if (key_str == 'x' or key_str == 'c') and not self.input_lock:
                    self.input_lock = not self.input_lock
                    self._HRICommandPub.publish("open")
            return


        # self._moveCommandPub.publish(key_str)

    def on_release(self,key):
        try :
            key_str = '{0}'.format(key.char)
        except :
            key_str = '{0}'.format(key)

        if self.input_lock:
            self.input_lock = not self.input_lock
            self._HRICommandPub.publish(key_str)

        


    def _transSubCallback(self,data):
        tr = TfMessgaeToTransform(Msg) #c++ 바인딩 된 부분인듯????
        self._savedTransform = tr

    def _getPosition(self,Transform):
        self._savedTransform = Transform
    




def main():
    simple_command_pub_sim = simple_command_pub_sim()

    rospy.init_node('zeus_position_logger', anonymous=True)

    try:
        rospy.spin()

    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main()        


