import rospy
import actionlib

from abc import ABC , abstractmethod
from std_msgs.msg import String

class endEffector(ABC):
    def __init__(self):
        self._lidState = "close"

    @abstractmethod
    def open(self) :
        pass

    @abstractmethod    
    def close(self) :   
        pass
    
    def getState(self) :
        return self._lidState

    def setState(self, command):
        if command in ['open','close'] :
            self._lidState = command
        else :
            print("Wrong EE Command") 