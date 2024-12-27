class Weapon:
    def __init__(self, name, Dmg, Stamina):
        self._dmg = Dmg
        self._stamina = Stamina
        self.name = name
    def attack1(self, enemy):
        enemy._hp -= self._dmg[0]
    def attack2(self, enemy):
        enemy._hp -= self._dmg[1]
    def GetWeaponName(self):
        return self.name
        
    

class Cutlass(Weapon):
    def __init__(self, name, Dmg, Stamina):
        super().__init__(name, Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A basic blade with blunt edges. The only weapon you could find.")
    def attack1_msg(self):
        print("You slash at your foe.")
    def attack2_msg(self):
        print("With a swift flick, you deliver a sharp strike.")
class Mace(Weapon):
    def __init__(self, name, Dmg, Stamina):
        super().__init__(name, Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A heavy, blunt weapon designed for crushing blows. Capable of very large bursts of damage.")
    def attack1_msg(self):
        print("You puncture your enemy with a brutal thrash.")
    def attack2_msg(self):
        print("The mace swings down with a bone-crushing force")

class Katana(Weapon):
    def __init__(self, name, Dmg, Stamina):
        super().__init__(name, Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A versatile blade crafted with care. Capable of very swift attacks")
    def attack1_msg(self):
        print("You dice the enemy.")
    def attack2_msg(self):
        print("In a split second, your katana is resheathed as swift, fluid strikes lacerate your foe.")
    # Weapon Attacks go here

class Scythe(Weapon):
    def __init__(self, name, Dmg, Stamina):
        super().__init__(name, Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A curved blade forged for reaping, repurposed for combat. Capable of large and slightly quick attacks.")
    def attack1_msg(self):
        print("Your curved blade cleaves through your foe.")
    def attack2_msg(self):
        print("Your wicked blade reaps your foe, mercilessly scissoring the misty air.")
    # Weapon Attacks go here

class Club(Weapon):          

    def __init__(self, name, Dmg, Stamina):
        super().__init__(name, Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A very heavy hunk of metal, too large to be called a sword. Capable of extremely large attacks.")
    def attack1_msg(self):
        print("Your club crashes down on the foe with a bone-crushing blow.")
    def attack2_msg(self):
        print("With a powerful swing, the club devastates the enemy, delivering shockwaves through the air.")
    # Weapon Attacks go here

        
                    #DAMAGE  STAMINA



cutlass = Cutlass("Cutlass", (6, 8), (10, 15))
mace = Mace("Mace", (10, 15), (20, 25))
katana = Katana("Katana", (8, 12), (10, 15))
scythe = Scythe("Scythe", (12, 16), (15, 20))
club = Club("Club", (20, 25), (30, 40))



