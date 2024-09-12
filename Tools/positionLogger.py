
import sys

sys.path.append('/home/sjlab3090/Desktop/2024_ZEUS/')

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

        self._moveCommandPub      =      rospy.Publisher("/zeus/webots/simpleMoveCommand",String, queue_size= 10)


    def on_press(self,key) :
        try :
            key_str = '{0}'.format(key.char)
        except :
            key_str = '{0}'.format(key)

        self._moveCommandPub.publish(key_str)

    def on_release(self,key):
        if key == keyboard.Key.esc:
            return False    


    def _transSubCallback(self,data):
        tr = TfMessgaeToTransform(Msg)
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


