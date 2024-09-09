from abc import ABC, abstractmethod
from .fsm import FSM
from .endeffector import endEffector

import rospy




class Agent(ABC):

    def __init__(self,name):
        self._name = name

        # Init Pose should be updated (in config)
        self._initPose = None

        self._jointNames = []

        self._fsm = FSM()

        self._EE = endEffector()


        self.rate1 = rospy.Rate(10)
        
        self.rate2 = rospy.Rate(20)

        self.rate3 = rospy.Rate(30)


        self._curJoint = None

        self._curTrans = None

        self._commandJoint = None

        self._commandTrans = None



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



# ------------------------- Internal param Setting ----------------------

    def setJointNames(self,namelist):
        
        self._jointNames = namelist






        
        

    

