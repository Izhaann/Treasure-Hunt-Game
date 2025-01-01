from EnemiesClass import Enemy
from CombatStateMachines import CombatTurnAlternatingStateMachine, CombatTurnBase, PlayerBuffStateMachine
from PlayerClass import Player
from WeaponClass import Weapon
import questionary
from PlayerInventoryClass import Bag
from GameDevelopmentToolsFunctions import clear_console, TimerSleep
from EnemiesClass import skeleton
import random
import sys

                                                                            # Strength Implementation





# Create a function to check Buffs
# Create If statements to link the players current buff to the state they are on
#   If strength:
#       PlayerBuffEffectStateMachine.TransitionState(Strength)
#  etc...
#
#   use the same if statement to switch off the players strength over time:
    #   keep a variable of the players current turn
    #   Subtract this number from the players current turn each turn
    #   Once this number gets to a certain number, turn off the buff
    #   reset the turns
    #   use the function with the if statements to change the state which effects the players buff




PlayerBuffStateMachineRef = PlayerBuffStateMachine()

CombatTurnAlternatingStateMachineRef = CombatTurnAlternatingStateMachine(Player)

class CombatClass(CombatTurnBase, CombatTurnAlternatingStateMachine):
    def __init__(self):
        pass
    
    
    




    def EnemyAttack(self, enemy):
        attackNumber = random.randint(1,3)
        if Player._defended == True:
            enemy._dmg[0] //= 2
            enemy._dmg[1] //= 2
        if attackNumber == 1:
            enemy.attack1(Player)
        elif attackNumber == 2:
            enemy.attack1(Player)
        else:
            enemy.attack2(Player)


        if Player._defended == True:
            enemy._dmg[0] *= 2
            enemy._dmg[1] *= 2
            Player._defended = False






    def CheckCurrentPlayerBuff(self):
        if Player._strength == True:
            return (x * 1.2 for x in Player.current_weapon._dmg)
            
    def ResetEnemy(self, enemy):
        enemy._hp = enemy._maxHP

        



    clear_console()
    def CombatMenu(self, enemy):


        

        self.CheckCurrentPlayerBuff()



        attackOption1 = f"{Player.current_weapon._attackname1}      |      Damage: {Player.current_weapon._dmg[0]}      Stamina:  {Player.current_weapon._stamina[0]}"
        attackOption2 = f"{Player.current_weapon._attackname2}      |      Damage: {Player.current_weapon._dmg[1]}      Stamina:  {Player.current_weapon._stamina[1]}"
        self.InCombat = True

        if CombatTurnAlternatingStateMachineRef.currentState == "enemy":
            self.EnemyAttack(enemy)

            CombatTurnAlternatingStateMachineRef.IncrementState()
            TimerSleep()
        
        
        if enemy._hp <= 0:
            clear_console()
            print(f"You have defeated the {enemy.get_name()}")
            TimerSleep()
            CombatTurnAlternatingStateMachineRef.EndStateMachine()
            self.InCombat = False

        if Player._hp < 0:
            clear_console()
            print(f"You were slain by the {enemy.get_name()}")
            print("Take this time to reflect upon your mistakes.")
            TimerSleep()
            TimerSleep()
            TimerSleep()
            sys.exit()
            





                                                                    # MENU
        clear_console()
        if self.InCombat == True:
            print(f"Enemy HP: {enemy._hp}")
            print(Player.get_player_stats())
            CombatChoice = questionary.select(
                    "What would you like to do?",
                    choices = [
                        "Attack",
                        "Bag",
                        "Defend"
                    ]).ask()

                                                                                # ATTACKING
            if CombatChoice == "Attack":
                AttackChoice = questionary.select(
                    "What attack will you do?",
                    choices = [attackOption1,
                            attackOption2,
                            "Back"
                            
                        

                    ]).ask()
                
                
                if AttackChoice == attackOption1:
                    print(Player.current_weapon.attack1_msg())
                    Player.attack_1(enemy)
                    CombatTurnAlternatingStateMachineRef.IncrementState()
            

                if AttackChoice == attackOption2:
                    print(Player.current_weapon.attack2_msg())
                    Player.attack_2(enemy)
                    CombatTurnAlternatingStateMachineRef.IncrementState()
                self.CombatMenu(enemy)

                if AttackChoice == "Back":
                    self.CombatMenu(enemy)
            if CombatChoice == 'Bag':
                Bag.OpenInventory()
                self.CombatMenu(enemy)
                
                
                

            if CombatChoice == 'Defend':
                Player.defend()
                print("You Defended against the enemies staggering blow")
                CombatTurnAlternatingStateMachineRef.IncrementState()
                TimerSleep()
                self.CombatMenu(enemy)
            

                

            


Combat = CombatClass()
#Combat.CombatMenu(skeleton)
#Player.equip(Player.current_weapon)
#print(Player.dmg)


