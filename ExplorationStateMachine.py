class ExplorationBaseState:
    def __init__(self, context):
        self.context = context
    
    def OnEnter(self):
        pass

    def OnUpdate(self):
        pass
    
    def OnExit(self):
        pass

class RoomState(ExplorationBaseState):
    def OnEnter(self):
        pass

    def OnUpdate(self):
        pass

    def OnExit(self):
        pass

class IslandSwitcherState(ExplorationBaseState):
    def OnEnter(self):
        pass

    def OnUpdate(self):
        pass

    def OnExit(self):
        pass

class IdleExplorationState(ExplorationBaseState):
    def OnEnter(self):
        pass

    def OnUpdate(self):
        pass

    def OnExit(self):
        pass

class PlayerExplorationStateMachine:
    def __init__(self, player_ref):
        self.states = {
            "room" : RoomState(),
            "switch" : IslandSwitcherState(),
            "idle" : IdleExplorationState()

            }
        self.currentState = "idle"
        self.player_ref = player_ref
    
    def TransitionState(self):
        nextstate = self.states[self.currentState].OnEnter()
        if nextstate != self.currentState:
            self.currentState = nextstate
        return True
    