from .endeffector import endEffector 

import rospy

from std_msgs.msg import String

class webotsEE(endEffector) :
    
    def __init__(self) :

        self._eeCommandPub = rospy.Publisher('/zeus/webots/eeCommand',String,queue_size=10)
         
    def open(self) :
        msg = String('open')
        self._eeCommandPub.publish(msg)

    def close(self) :    
        msg = String('close')
        self._eeCommandPub.publish(msg)