from abc import ABC, abstractmethod




class Agent(ABC):

    def __init__(self,name):
        self.name = name

        # Init Pose should be updated (in config)
        self.initPose = None
        
        self.lidClosed = True

        self.state = 'idle'

        self.fsm = self._initialize_fsm()


 # ------------------------ FSM Initialization ------------------------

    def _initializeFsm_(self):

        return {
            'idle': {
                'hri_start' : 'hri_mod',
                'move': 'moving',
                'greet': 'greeting'
            },
            'hri_mod' : {
                'hri_end' : 'idle'
            },
            'moving': {
                'stop': 'idle',
                'shake': 'shaking',
            },
            'greeting': {
                'finish_greet': 'idle',
            },
            'shaking': {
                'finish_shake': 'moving',
            }
        }

    def handleEvent(self, event):

        if event in self.fsm[self.state]:
            new_state = self.fsm[self.state][event]
            print(f"Transitioning from {self.state} to {new_state} on event '{event}'")
            self.state = new_state
        else:
            print(f"Failed to handle '{event}' in state '{self.state}'")


#--------------------------- Action Part ----------------------

    @abstractmethod
    def initial_pose(self):
        self.movePose(self.initPose)

    @abstractmethod
    def movePose(self,Transform) :
        pass

    @abstractmethod
    def moveX(self,xDistance) :
        pass

    @abstractmethod
    def moveY(self,yDistance) :
        pass

    @abstractmethod
    def moveZ(self,zDistance) :
        pass

    @abstractmethod    
    def rotateX(self,xAngle)  :
        pass

    @abstractmethod    
    def rotateY(self,yAngle)  :
        pass

    @abstractmethod    
    def rotateZ(self,zAngle)  :
        pass

    @abstractmethod
    def openEE(self) :
        pass

    @abstractmethod
    def closeEE(self) :
        pass



# -------------------------------- High level movement ---------------------------

    @abstractmethod
    def shake(self) :
        pass

    @abstractmethod 
    def greetCustomer(self) :
        pass

    @abstractmethod
    def moveSetPose(self ,index):
        pass

    @abstractmethod
    def getSources(self, index) :
        # This motion should come back to pre-defined position
        pass    


# -------------------------- HRI Part -----------------------------

    @abstractmethod
    def say(self, sentence, show_display = False):
        pass

        
    @abstractmethod
    def listen(self, sentence, show_display = False):
        pass 

    @abstractmethod
    def filterSentence(self, sentence) :
        pass

    @abstractmethod
    def sendLLM_Sentence(self, sentence, show_display = False):
        pass

    @abstractmethod
    def getLLM_Response(self) :
        pass    
        
    @abstractmethod
    def checkWord(self, direction) :
        # Dirction == from customer , to customer
        pass

#------------------------------------------------------------------------

    @abstractmethod
    def selectMenu(self,source):
        pass






        
        

    

