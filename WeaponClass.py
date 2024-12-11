class Weapon:
    def __init__(self, Dmg, Stamina):
        self._dmg = Dmg
        self._stamina = Stamina
    def attack1(self, enemy):
        enemy._hp -= self._dmg[0]
    def attack2(self, enemy):
        enemy._hp -= self._dmg[1]
        
    

class Cutlass(Weapon):
    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A basic blade with blunt edges. The only weapon you could find.")
    def attack1_msg(self):
        print("You cut the enemy")
    def attack2_msg(self):
        print("You plunge at the enemy")

class Mace(Weapon):
    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A very heavy, spiked, iron ball. Capable of very large bursts of damage.")
    def attack1_msg(self):
        print("You swing your mace.")
    def attack2_msg(self):
        print("You charge your mace and throw it at the enemy")

class Katana(Weapon):
    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A versatile blade crafted with care. Capable of  very quick attacks")
    def attack1_msg(self):
        print("You slice the enemy")
    def attack2_msg(self):
        print("You drive your katana into the enemy")
    # Weapon Attacks go here

class Scythe(Weapon):
    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A heavy weapon, topped with a long, curved edge. Capable of large and  slight quick attacks.")
    def attack1_msg(self):
        print("You hack at the enemy")
    def attack2_msg(self):
        print("You slash at the enemy")
    # Weapon Attacks go here

class Club(Weapon):          

    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print("A very heavy hunk of metal, too large to be called a sword. Capable of extremely large attacks.")
    def attack1_msg(self):
        print("You swing at the enemy")
    def attack2_msg(self):
        print("You smash the enemy")
    # Weapon Attacks go here

        
                    #DAMAGE  STAMINA



cutlass = Cutlass((6, 8), (10, 15))
mace = Mace((10, 15), (20, 25))
katana = Katana((8, 12), (10, 15))
scythe = Scythe((12, 16), (15, 20))
club = Club((20, 25), (30, 40))



