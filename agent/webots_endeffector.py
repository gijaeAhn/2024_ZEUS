import endeffector 

import rospy

from std_msgs.msg import String

class webotsEE(endEffector) :
    
    def __init__(self) :

        self._eeCommandPub = rospy.Publisher('/zeus/webots/eeCommand',String,queue_size=10)
         
    def open(self) :
         pass

    def close(self) :    
        pass