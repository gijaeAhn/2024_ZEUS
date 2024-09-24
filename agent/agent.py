import sys
import os

home_dir = os.path.expanduser('~')

sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))




from abc          import ABC, abstractmethod
from .fsm         import FSM
from .endeffector import endEffector
from .tts         import TTS

import rospy

from config.config import *




class Agent(ABC):


    def __init__(self):
        

        # Init Pose should be updated (in config)
        self._initPose = None

        self._jointNames = []

        self._fsm = FSM()

        # self._EE = endEffector()


        self.rateFast = rospy.Rate(WebotsConfig.LONG_SLEEP)
        
        self.rateNormal = rospy.Rate(WebotsConfig.NORMAL_SLEEP)

        self.rateSlow = rospy.Rate(WebotsConfig.SHORT_SLEEP)


        self._curJoint = None

        self._curTrans = None

        self._commandJoint = None

        self._commandTrans = None

        # self._tts = TTS()



#--------------------------- Action Part ----------------------

    @abstractmethod
    def movePoseT(self,Transform) :
        pass

    @abstractmethod
    def movePoseA(self,Angle) :
        pass

    def moveInitpose(self):
        self.movePoseA(self.initPose)

    @abstractmethod
    def _moveX(self,xDistance) :
        pass

    @abstractmethod
    def _moveY(self,yDistance) :
        pass

    @abstractmethod
    def _moveZ(self,zDistance) :
        pass

    @abstractmethod    
    def _rotateX(self,xAngle)  :
        pass

    @abstractmethod    
    def _rotateY(self,yAngle)  :
        pass

    @abstractmethod    
    def _rotateZ(self,zAngle)  :
        pass

    @abstractmethod
    def _openEE(self) :
        pass

    @abstractmethod
    def _closeEE(self) :
        pass



# -------------------------------- High level movement ---------------------------

    # @abstractmethod
    # def shake(self) :
    #     pass

    # @abstractmethod 
    # def greetCustomer(self) :
    #     pass

    # @abstractmethod
    # def moveSetPose(self ,index):
    #     pass

    # @abstractmethod
    # def getSources(self, index) :
    #     # This motion should come back to pre-defined position
    #     pass    


# -------------------------- HRI Part -----------------------------

#     @abstractmethod
#     def say(self, sentence, show_display = False):
#         pass

        
#     @abstractmethod
#     def listen(self, sentence, show_display = False):
#         pass 

#     @abstractmethod
#     def filterSentence(self, sentence) :
#         pass

#     @abstractmethod
#     def sendLLM_Sentence(self, sentence, show_display = False):
#         pass

#     @abstractmethod
#     def getLLM_Response(self) :
#         pass    
        
#     @abstractmethod
#     def checkWord(self, direction) :
#         # Dirction == from customer , to customer
#         pass

# #------------------------------------------------------------------------

#     @abstractmethod
#     def selectMenu(self,source):
#         pass



# ------------------------- HRI ----------------------------------------

    def _say(self,sentence, show_display = False) :
        self._tts.say(sentence)
        if show_display:
            self._show_text(sentence)

    def _show_text(self,sentence) :
        pass    
    


# ------------------------- Internal param Setting ----------------------

    def setJointNames(self,namelist):
        
        self._jointNames = namelist






        
        

    

