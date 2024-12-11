import random
class Enemy():
    def __init__(self, HP, maxHP):
        self._hp = HP
        self._maxHP = maxHP

class Skeletons(Enemy):
    def __init__(self, HP, maxHP):
        super().__init__(HP, maxHP)
        self._dmg = ((random.randint(1, 2)), 3)
    def get_hp(self):
        return self._hp
    def appearance_msg(self):
        pass
        # appearance msg goes here
    def attack1(self, player):
        # msg goes here
        player._hp -= self._dmg[0]
    def attack2(self, player):
        # msg goes here
        player._hp -= self._dmg[1]


class Spiders(Enemy):
    def __init__(self, HP, maxHP):
        super().__init__(HP, maxHP)
        self._dmg = ((random.randint(1, 2)), 3)
    def get_hp(self):
        return self._hp
    def appearance_msg(self):
        pass
        # appearance msg goes here
    def attack1(self, player):
        # msg goes here
        player._hp -= self._dmg[0]
    def attack2(self, player):
        # msg goes here
        player._hp -= self._dmg[1]


class Ogres(Enemy):
    def __init__(self, HP, maxHP):
        super().__init__(HP, maxHP)
        self._dmg = ((random.randint(2, 3)), 4)
    def get_hp(self):
        return self._hp
    def appearance_msg(self):
        pass
        # appearance msg goes here
    def attack1(self, player):
        # msg goes here
        player._hp -= self._dmg[0]
    def attack2(self, player):
        # msg goes here
        player._hp -= self._dmg[1]

class BerserkerFairies(Enemy):
    def __init__(self, HP, maxHP):
        super().__init__(HP, maxHP)
        self._dmg = ((random.randint(3, 4)), 5)
    def get_hp(self):
        return self._hp
    def appearance_msg(self):
        pass
        # appearance msg goes here
    def attack1(self, player):
        # msg goes here
        player._hp -= self._dmg[0]
    def attack2(self, player):
        # msg goes here
        player._hp -= self._dmg[1]

class Pirates(Enemy):
    def __init__(self, HP, maxHP):
        super().__init__(HP, maxHP)
        self._dmg = ((random.randint(4, 5)), 6)
    def get_hp(self):
        return self._hp
    def appearance_msg(self):
        pass
        # appearance msg goes here
    def attack1(self, player):
        # msg goes here
        player._hp -= self._dmg[0]
    def attack2(self, player):
        # msg goes here
        player._hp -= self._dmg[1]

skeleton = Skeletons(10,10)
spider = Spiders(10, 10)
ogres = Ogres(15, 15)
berserkerfairies = BerserkerFairies(20, 20)
pirates = Pirates(20, 20)