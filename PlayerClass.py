from WeaponClass import stick, cutlass, mace, katana, scythe, club
from EnemiesClass import skeleton, spider, ogres, pirates, elves, pirate_king
from rich.console import Console
from rich.progress import Progress, TextColumn
from LocationClasses import Location, SkullyWagShores, VenomousCove, GhastlyReef, WhisperingHollow, Brutalith, BlackWater, GodValley
console = Console()


 
class Person():
    def __init__(self, HP, Stamina, Dmg, maxHP, maxStamina, maxDmg):
        self._hp = HP
        self._stamina = Stamina
        self.dmg = Dmg
        self._maxHP = maxHP
        self._maxStamina = maxStamina
        self._maxDmg = maxDmg
        self.current_weapon = stick
        self._defended = False
        self.player_combat_turn = True
        self._strength = True
        self._currentLocation = Brutalith
        self.name = ""



    def get_player_stats(self):
        print("")
        with Progress(console=console) as progress:
            progress.add_task("[bold red]HP", total=self._maxHP, completed=self._hp)   
            progress.add_task("[blue]Stamina", total=self._maxStamina, completed=self._stamina)

        print(f"{self._hp}/{self._maxHP} HP")
        print(f"{self._stamina}/{self._maxStamina} Stamina")
        return ""
    

    def set_dmg(self, damage):
        self._dmg = damage._dmg
    def add_hp(self, HP):
        self._hp += HP
    def get_hp(self):
        print(self._hp)
    def set_hp(self, HP):
        self._hp = HP._hp
    def add_stamina(self, stamina):
        self._stamina += stamina
    def get_stamina(self):
        print(self._stamina)



        
        


    #  COMBAT FUNCTIONS







    def attack_1(self, enemy):
        self.current_weapon.attack1(enemy)
        self._stamina -= self.current_weapon._stamina[0]
        self.player_combat_turn = False
    def attack_2(self, enemy):
        self.current_weapon.attack2(enemy)
        self._stamina -= self.current_weapon._stamina[1]
        self.player_combat_turn = False
    
    
    def defend(self):
        self._defended = True
        self._stamina += 20


    def equip(self, weapon):
        self.set_dmg(weapon)
        self.current_weapon = weapon
        



    # HP, Stamina, Dmg, maxHP, maxStamina, maxDmg
Player = Person(50, 50, 50, 50, 50, 50)
Player2 = Person(50, 50, 50, 50, 50, 50)