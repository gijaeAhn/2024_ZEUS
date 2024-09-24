class FSM() :

    def __init__(self):
        

        self._state = 'idle'
        self._stateTable = self._initializeStates()

    def _initializeStates(self) :

        return {
            'idle': {
                'hri_start' : 'hri_idle',
                'greet': 'greeting'
            },
            'greeting': {
                'finish_greet': 'idle',
            },
            'hri_idle' : {  
                'speak'    : 'speaking',
                'listen'   : 'listening',
                'get_menu' : 'moving'
            },
            'speaking' :{
                'stop'     : 'hri_idle'
            },
            'listening' :{
                'stop'     : 'hri_idle'
            },
            'moving': {
                'stop': 'idle',
                'shake': 'shaking',
                'serve_menu' : 'idle'
            },
            'shaking': {
                'finish_shake': 'moving',
            }
        }
    
    def handleEvent(self,event) :

<<<<<<< HEAD
        if event in self.stateTable_[self.state]:
            new_state = self.stateTable_[self.state][event]
            print(f"Transitioning from {self.state} to {new_state} on event '{event}'")
            self.state = new_state
=======
        if event in self._stateTable[self._state]:
            new_state = self._stateTable[self._state][event]
            print(f"Transitioning from {self._state} to {new_state} on event '{event}'")
            self._state = new_state
>>>>>>> 6535e9b93b832376daa2b8fd13e71f0c69797878
        else:
            print(f"Failed to handle '{event}' in state '{self._state}'")

    def checkState(self,event) :
        return self._state == event
    
    def getState(self) :
        return self._state

