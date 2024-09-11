import rospy
import actionlib

from abc import ABC , abstractmethod
from std_msgs.msg import String

class endEffector(ABC):
    def __init__(self):


        self._lidState = "open"

    def _eeCallback(self,data) :

        if data == 'open' :
            self.open()
            return True
        elif data == 'close':
            self.close()
            return True
        else :
            print("Wrong EE Command")
            return False 


    @abstractmethod
    def open(self) :
        pass

    @abstractmethod    
    def close(self) :   
        pass

    
    def getState(self) :
        return self._lidState 