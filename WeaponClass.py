
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
        print()
    def attack1_msg(self):
        pass
    def attack2_msg(self):
        pass

class Mace(Weapon):
    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print()
    def attack1_msg(self):
        pass
    def attack2_msg(self):
        pass
    # Weapon Attacks go here

class Katana(Weapon):
    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print()
    def attack1_msg(self):
        pass
    def attack2_msg(self):
        pass
    # Weapon Attacks go here

class Scythe(Weapon):
    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print()
    def attack1_msg(self):
        pass
    def attack2_msg(self):
        pass
    # Weapon Attacks go here

class Club(Weapon):
    def __init__(self, Dmg, Stamina):
        super().__init__(Dmg, Stamina)
    def get_dmg(self):
        return self.dmg
    def get_desc():
        print()
    def attack1_msg(self):
        pass
    def attack2_msg(self):
        pass
    # Weapon Attacks go here

        
                    #DAMAGE  STAMINA
cutlass = Cutlass((6, 8), (10, 15))
mace = Mace((10, 15), (20, 25))
katana = Katana((8, 12), (10, 15))
scythe = Scythe((12, 16), (15, 20))
club = Club((20, 25), (30, 40))



