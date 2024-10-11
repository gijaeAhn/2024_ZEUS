class FSM() :

    def __init__(self):
        

        self._state      = 'idle'
        self._stateTable = self._initializeStates()
        self._events     = ['hri_start','greet', 'finish_greet', 'speak', 'listen', 'get_menu', 'stop', 'shake','serve_menu', 'finish_shake'] 

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

        if event in self._stateTable[self._state]:
            new_state = self._stateTable[self._state][event]
            print(f"Transitioning from {self._state} to {new_state} on event '{event}'")
            self._state = new_state
        else:
            print(f"Failed to handle '{event}' in state '{self._state}'")

    def checkState(self,event) :
        return self._state == event
    
    def getState(self) :
        return self._state

