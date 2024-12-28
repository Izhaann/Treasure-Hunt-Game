from EnemiesClass import Enemy
from CombatStateMachines import CombatTurnAlternatingStateMachine, CombatTurnBase
from PlayerClass import Player
from WeaponClass import Weapon
import questionary
from GameDevelopmentFunctionTools import clear_console
from EnemiesClass import skeleton


CombatTurnAlternatingStateMachineRef = CombatTurnAlternatingStateMachine(Player)
CombatTurnAlternatingStateMachineRef.TransitionState()
class CombatClass(CombatTurnBase, CombatTurnAlternatingStateMachine):
    def __init__(self):
        self.TotalTurns = 0
        self.TotalPlayerTurns = 0
        self.TotalEnemyTurns = 0






    def CombatMenu(self, enemy):
        print(f"Enemy HP: {enemy._hp}")
        print(Player.get_player_stats())
        CombatChoice = questionary.select(
                "What would you like to do?",
                choices = [
                    "Attack",
                    "Bag",
                    "Defend"
                ]).ask()
        
        if CombatChoice == "Attack":
            AttackChoice = questionary.select(
                "What attack will you do?",
                choices = [Player.current_weapon._attackname1,
                           Player.current_weapon._attackname2,
                           
                    

                ]).ask()
            if AttackChoice == Player.current_weapon._attackname1:
                print(Player.current_weapon.attack1_msg())
                Player.current_weapon.attack1(enemy)
                print(CombatTurnAlternatingStateMachineRef.currentState)
            


Combat = CombatClass()
Combat.CombatMenu(skeleton)

