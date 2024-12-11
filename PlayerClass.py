from CombatStateMachines import PlayerBuffStateMachine
from WeaponClass import cutlass, mace, katana, scythe, club
from EnemiesClass import skeleton, spider, ogres, pirates, berserkerfairies, pirate_king
from rich.console import Console
from rich.progress import Progress, TextColumn
console = Console()


 
class Person(PlayerBuffStateMachine):
    def __init__(self, HP, Stamina, Dmg, maxHP, maxStamina, maxDmg):
        super().__init__(self)
        self._hp = HP
        self._stamina = Stamina
        self._dmg = Dmg
        self._maxHP = maxHP
        self._maxStamina = maxStamina
        self._maxDmg = maxDmg
        self._currentweapon = cutlass
        self._defended = False
        self._player_combat_turn = True
        self._strength = False
    def get_player_stats(self):
        with Progress(console=console) as progress:
            progress.add_task("[bold red]HP", total=self._maxHP, completed=self._hp)
            progress.add_task("[blue]Stamina", total=self._maxStamina, completed=self._stamina)
    def set_dmg(self, damage):
        self._dmg = damage._dmg
    def add_hp(self, HP):
        self._hp += HP
    def get_hp(self):
        print(self._hp)
    def add_stamina(self, stamina):
        self._stamina += stamina._stamina
    def set_hp(self, HP):
        self._hp = HP._hp
    def add_stamina(self, stamina):
        self._stamina += stamina
    def get_stamina(self):
        print(self._stamina)



        
        


    #  COMBAT FUNCTIONS







    def attack_1(self, enemy):
        self._current_weapon.attack1(enemy)
        self._stamina -= self._current_weapon._stamina[0]
        self._player_combat_turn = False
    def attack_2(self, enemy):
        self._current_weapon.attack2(enemy)
        self._stamina -= self._current_weapon._stamina[1]
        self._player_combat_turn = False
    
    
    def defend(self):
        self._defended = True


    def equip(self, weapon):
        self.set_dmg(weapon)
        self._current_weapon = weapon
        

Player = Person(50, 50, 0, 50, 50, 50)
Player2 = Person(50, 50, 0, 50, 50, 50)
Player.equip(katana)
Player.attack_1(skeleton)
# skeleton.get_hp()
# Player.get_stamina()
pirate_king.attack1(Player)
Player.get_hp()
Player.get_player_stats()