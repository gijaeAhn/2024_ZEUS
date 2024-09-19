
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

        self._savedTransform      =      None

        self._transSub            =      rospy.Subscriber("/zeus/webots/realTF", tfMessage, self._transSubCallback) 

        self._moveCommandPub      =      rospy.Publisher("/zeus/webots/simpleMoveCommand",String, queue_size= 10) #키 값을 받아서 WebotClient에게 넘겨주는 Publisher, 키가 눌릴때마다 그 값이 webotClient 에게 전달됨.

        self._HRICommandPub       =      rospy.Publisher("HRICommand", String, queue_size=1) #modified by ms

     

    def on_press(self,key) :
        try :
            key_str = '{0}'.format(key.char)
        except :
            key_str = '{0}'.format(key)
        print(key_str)
        if key_str == 'o' or key_str == 'c':
            self._HRICommandPub.publish(key_str)
        else:
            self._moveCommandPub.publish(key_str)
    
        # self._moveCommandPub.publish(key_str)

    def on_release(self,key):
        # if key == keyboard.Key.esc:
        #     return False    
        pass


    def _transSubCallback(self,data):
        tr = TfMessgaeToTransform(Msg) #c++ 바인딩 된 부분인듯????
        self._savedTransform = tr

    def _getPosition(self,Transform):
        self._savedTransform = Transform
    




def main():
    zeusPositionLogger = positionLogger()

    rospy.init_node('zeus_position_logger', anonymous=True)

    try:
        rospy.spin()

    except KeyboardInterrupt:
        print("Shutting down")

if __name__ == '__main__':
    main()        


