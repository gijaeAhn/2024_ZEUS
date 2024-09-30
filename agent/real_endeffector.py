from .endeffector import endEffector 

import rospy

from std_msgs.msg import String

class realEE(endEffector) :
    
    def __init__(self) :

        endEffector.__init__(self)
        self._eeCommandPub = rospy.Publisher('/zeus/real/gripperCommand',String,queue_size=10)
        
         
    def open(self) :
        self.setState('open')
        msg = String('x')
        self._eeCommandPub.publish(msg)

    def close(self) : 
        self.setState('close')   
        msg = String('z')
        self._eeCommandPub.publish(msg)

    def getState(self):
        return super().getState() 