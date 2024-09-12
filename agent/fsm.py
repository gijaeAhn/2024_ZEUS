class FSM() :

    def __init__(self):
        
        self.state_ = 'idle'
        self.stateTable_ = self._initialize_states()


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
                'listen'   : 'listeing',
                'get_menu' : 'moving'
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

        if event in self.fsm[self.state]:
            new_state = self.fsm[self.state][event]
            print(f"Transitioning from {self.state} to {new_state} on event '{event}'")
            self.state = new_state
        else:
            print(f"Failed to handle '{event}' in state '{self.state}'")

    def checkState(self,event) :
        return self.state == event

