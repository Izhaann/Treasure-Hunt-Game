import itertools
from PlayerClass import Player
class PlayerStateBase:
    def __init__(self, context):
        self.context = context

    def OnEnter(self):
        pass

class Tired_State(PlayerStateBase):
    def OnEnter(self):
        Player.dmg // 1.5
        if Player._stamina > 10:
            print("act")
            return "active"
        else:
            return "tired"
class Active_State(PlayerStateBase):
    def OnEnter(self):
        if Player._stamina <= 10:
            print("tir")
            return "tired"
        else:
            return "active"
class Strength_State(PlayerStateBase):
    def OnEnter(self):
        while Player._strength:
            Player.dmg * 1.2
        if Player._strength != True:
            print("str")
            
            return "active"
        else:
            return "strength"
class PlayerBuffStateMachine:
    def __init__(self):
        self.states = {
            "tired" : Tired_State(self),
            "active" : Active_State(self),
            "strength": Strength_State(self),
            }
        self.currentState = "active"
        

    def TransitionState(self):
        nextstate = self.states[self.currentState].OnEnter()
        if nextstate != self.currentState:
            self.currentState = nextstate
        return True
    
    def SwitchState(self, state):
        if state != self.currentState:
            self.currentState = state
        




                                            # TURN TRACKER STATE MACHINE




class CombatTurnBase:
    def __init__(self, context):
        self.context = context
        self.turnCount = 0

    def OnEnter(self):
        pass
    
    def OnExit(self):
        pass

    def IncrementTurnCount(self):
        self.turnCount += 1

class EnemyTurn(CombatTurnBase):
    def OnEnter(self):
        #print(f"Starting Enemy Turn {self.turnCount}")
        pass
    def OnExit(self):
        #print("Ending Enemy Turn")
        pass

class PlayerTurn(CombatTurnBase):
    def OnEnter(self):
        #print(f"Starting Player Turn {self.turnCount}")
        pass
    def OnExit(self):
        #print("Ending Player Turn")
        pass
class CombatTurnAlternatingStateMachine:
    def __init__(self, player_ref):
        self.states = {
            "enemy" : EnemyTurn(self),
            "player" : PlayerTurn(self),
        }
        self.currentState = "player" if player_ref.player_combat_turn else "enemy"
        self.iterStates = itertools.cycle(self.states.keys())

        self._player_ref = player_ref

        self.StartState(self.currentState)

    def StartState(self, state):
        stateInstance = self.states[state]
        stateInstance.IncrementTurnCount()
        stateInstance.OnEnter()

    def IncrementState(self):
        self.states[self.currentState].OnExit()

        nextState = next(self.iterStates)
        self.currentState = nextState

        self.StartState(self.currentState)

    def EndStateMachine(self):
        self.states[self.currentState].OnExit()
    
    


