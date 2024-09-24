
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





class positionLogger :

    def __init__(self):

        keyListener               =      keyboard.Listener(on_press= self.on_press, on_release= self.on_release)
        keyListener.start()

        self._moveCommandPub      =      rospy.Publisher("/zeus/real/simpleMoveCommand" ,String, queue_size= 1)
        self._gripperPub      =      rospy.Publisher("/zeus/real/gripperCommand", String, queue_size=1)

    def on_press(self,key) :
        try :
            key_str = '{0}'.format(key.char)
        except :
            key_str = '{0}'.format(key)

        if key_str in ('w', 'a', 's', 'd', 'q', 'e', 'i', '0', '1', '2', '3', '4'):
            self._moveCommandPub.publish(key_str)
        elif key_str in ('x', 'c'):
            self._gripperPub.publish(key_str)

    def on_release(self,key):
        if key == keyboard.Key.esc:
            return False    



def main():
    zeusPositionLogger = positionLogger()

    rospy.init_node('zeus_position_logger', anonymous=True)

    try:
        rospy.spin()

    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main()        


