class Weapon:
    def __init__(self, name, Dmg, Stamina, description, AttackName1, AttackName2):
        self._dmg = Dmg
        self._stamina = Stamina
        self.name = name
        self.desc = description
        self._attackname1 = AttackName1
        self._attackname2 = AttackName2
    def attack1(self, enemy):
        enemy._hp -= self._dmg[0]
    def attack2(self, enemy):
        enemy._hp -= self._dmg[1]
    def get_name(self):
        return self.name
    def get_desc(self):
        return self.desc
    
#
class Stick(Weapon):
    def __init__(self, name, Dmg, Stamina, description, AttackName1, AttackName2):
        super().__init__(name, Dmg, Stamina, description, AttackName1, AttackName2)
    def get_dmg(self):
        return self.dmg
    def attack1_msg(self):
        print("You deliver a sharp thrust with the end of your stick.")
        return ""
    def attack2_msg(self):
        print("You thwart the enemy with your blunt weapon")
        return ""




class Cutlass(Weapon):
    def __init__(self, name, Dmg, Stamina, description, AttackName1, AttackName2):
        super().__init__(name, Dmg, Stamina, description, AttackName1, AttackName2)
    def get_dmg(self):
        return self.dmg
    def attack1_msg(self):
        print("You slash at your foe.")
        return ""
    def attack2_msg(self):
        print("With a swift flick, you deliver a sharp strike.")
        return ""
class Mace(Weapon):
    def __init__(self, name, Dmg, Stamina, description, AttackName1, AttackName2):
        super().__init__(name, Dmg, Stamina ,description, AttackName1, AttackName2)
    def get_dmg(self):
        return self.dmg
    def attack1_msg(self):
        print("You puncture your enemy with a brutal thrash.")
        return ""
    def attack2_msg(self):
        print("The mace swings down with a bone-crushing force")
        return ""

class Katana(Weapon):
    def __init__(self, name, Dmg, Stamina, description, AttackName1, AttackName2):
        super().__init__(name, Dmg, Stamina ,description, AttackName1, AttackName2)
    def get_dmg(self):
        return self.dmg
    def attack1_msg(self):
        print("You dice the enemy.")
        return ""
    def attack2_msg(self):
        print("In a split second, your katana is resheathed as a swift, fluid strike lacerates your foe.")
        return ""
    # Weapon Attacks go here

class Scythe(Weapon):
    def __init__(self, name, Dmg, Stamina, description, AttackName1, AttackName2):
        super().__init__(name, Dmg, Stamina ,description, AttackName1, AttackName2)
    def get_dmg(self):
        return self.dmg
    def attack1_msg(self):
        print("Your curved blade cleaves through your foe.")
        return ""
    def attack2_msg(self):
        print("Your wicked blade reaps your foe, mercilessly scissoring the misty air.")
        return ""
    # Weapon Attacks go here

class Club(Weapon):          

    def __init__(self, name, Dmg, Stamina, description, AttackName1, AttackName2):
        super().__init__(name, Dmg, Stamina ,description, AttackName1, AttackName2)
    def get_dmg(self):
        return self.dmg
    def attack1_msg(self):
        print("Your club crashes down on the foe with a bone-crushing blow.")
        return ""
    def attack2_msg(self):
        print("With a powerful swing, the club devastates the enemy, delivering shockwaves through the air.")
        return ""
    # Weapon Attacks go here

        
                    #DAMAGE  STAMINA



stick = Stick("Stick", (100, 5), (5, 8), "A small yet powerful weapon crafted by Mother Mature herself. The only weapon you could find", "Poke", "Thwart")
cutlass = Cutlass("Cutlass", (4, 6), (6, 10), "A basic blade with blunt edges.", "Slash", "Stab")
mace = Mace("Mace", (9, 13), (15, 20), "A heavy, blunt weapon designed for crushing blows. Capable of very large bursts of damage.", "Thrash", "Swing")
katana = Katana("Katana", (8, 12), (10, 15), "A versatile blade crafted with care. Capable of very swift attacks", "Dice", "Strike")
scythe = Scythe("Scythe", (11, 14), (20, 25), "A curved blade forged for reaping, repurposed for combat. Capable of large and slightly quick attacks.", "Cleave", "Carve")
club = Club("Club", (15, 20), (25, 30), "A very heavy hunk of metal, too large to be called a sword. Capable of extremely large attacks.", "Crush", "Smash")



