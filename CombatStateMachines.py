
class PlayerStateBase:
    def __init__(self, context):
        self.context = context

    def OnEnter(self):
        pass

class Tired_State(PlayerStateBase):
    def OnEnter(self):
        self.player_ref._dmg // 1.5
        if self.player_ref._stamina > 10:
            print("act")
            return "active"
        else:
            return "tired"
class Active_State(PlayerStateBase):
    def OnEnter(self):
        if self.player_ref._stamina <= 10:
            print("tir")
            return "tired"
        else:
            return "active"
class Strength_State(PlayerStateBase):
    def OnEnter(self):
        self.player_ref._dmg * 1.2
        if self.player_ref._strength != True:
            print("str")
            
            return "tired"
        else:
            return "strength"
class PlayerBuffStateMachine:
    def __init__(self, player_ref):
        self.states = {
            "tired" : Tired_State(self),
            "active" : Active_State(self),
            "strength": Strength_State(self),
            }
        self.currentState = "active"
        self.player_ref = player_ref

    def TransitionState(self):
        nextstate = self.states[self.currentState].OnEnter()
        if nextstate != self.currentState:
            self.currentState = nextstate
        return True




                                            # TURN TRACKER STATE MACHINE



class CombatTurnBase:
    def __init__(self, context, player_ref):
        self.context = context
        self.player_ref = player_ref
    def OnEnter(self):
        pass

class EnemyTurn(CombatTurnBase):
    def OnEnter(self):
        if self.player_ref.player_combat_turn:
            return "player"
        return "enemy"
class PlayerTurn(CombatTurnBase):
    def OnEnter(self):
        if not self.player_ref.player_combat_turn:
            return "enemy"
        return "player"
class CombatTurnAlternatingStateMachine:
    def __init__(self, player_ref):
        self.states = {
            "enemy" : EnemyTurn(self, player_ref),
            "player" : PlayerTurn(self, player_ref),
            }
        self.currentState = "player" if player_ref.player_combat_turn else "enemy"
        self.TransitionState()

    def TransitionState(self):
        while True:
            nextstate = self.states[self.currentState].OnEnter()
            if nextstate != self.currentState:
                self.currentState = nextstate
                break
            else:
                break
    
    



class player:
    def __init__(self):
        self.player_combat_turn = True

Player = player()
machine = CombatTurnAlternatingStateMachine(Player)

        
