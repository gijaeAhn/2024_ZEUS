
import sys
import os

home_dir = os.path.expanduser('~')

sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))

#from utils.transformTotf import *

import rospy 

from pynput import keyboard

from lib.zeus_kinematics import *


from sensor_msgs.msg import JointState

from tf.msg import tfMessage
from std_msgs.msg   import String





class positionLogger :

    def __init__(self):

        self.exist_user = False

        keyListener               =      keyboard.Listener(on_press= self.on_press, on_release= self.on_release)
        keyListener.start()

        self._moveCommandPub      =      rospy.Publisher("/zeus/real/simpleMoveCommand" ,String, queue_size= 1)
        self._gripperPub      =      rospy.Publisher("/zeus/real/gripperCommand", String, queue_size=1)
        
        self._HRICommandPub       =      rospy.Publisher("HRICommand", String, queue_size=1) #modified by ms

        self.GreetingPub          =     rospy.Publisher("greeting_signal", String, queue_size=1)
        
        self.ByePub               =     rospy.Publisher("bye_signal", String, queue_size=1)

        self.input_lock           =      False







    def on_press(self,key) :
        try :
            key_str = '{0}'.format(key.char)
        except :
            key_str = '{0}'.format(key)
        
        print(key_str)
        
        if key_str in ('w', 'a', 's', 'd', 'q', 'e',     'v','b','n','f','g','h',      '0', '1', '2', '3', '4', '5', '6', '7', '8','9',    'r', 't',     'o','p'):
            self._moveCommandPub.publish(key_str)
        elif key_str in ('n', 'm'): #n => open, m => close
            self._gripperPub.publish(key_str)

        elif key_str in ('z', 'x', 'c'):
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


    def on_release(self,key):
        if key == keyboard.Key.esc:
            return False    
        
        try :
            key_str = '{0}'.format(key.char)
        except :
            key_str = '{0}'.format(key)

        if self.input_lock:
            self.input_lock = not self.input_lock
            self._HRICommandPub.publish(key_str)



def main():
    zeusPositionLogger = positionLogger()

    rospy.init_node('zeus_position_logger', anonymous=True)

    try:
        rospy.spin()

    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main()        


