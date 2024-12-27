import random

class Enemy():
    def __init__(self, HP, maxHP, appearance_msg):
        self._hp = HP
        self._maxHP = maxHP
        self._appearance_msg = appearance_msg
    def get_hp(self):
        return self._hp
    def appearance_msg(self):
        return self._appearance_msg



class Skeletons(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP, maxHP, appearance_msg)
        self._dmg = ((random.randint(1, 2)), 3)
   
    def attack1(self, player):
        print("The skeleton punches you.")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The skeleton threw a bone at you.")
        player._hp -= self._dmg[1]

class Spiders(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP,maxHP, appearance_msg)
        self._dmg = ((random.randint(1, 2)), 3)
   
    def attack1(self, player):
        print("The spider sinks his fangs into you.")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The spider spits venom in your face.")
        player._hp -= self._dmg[1]

class Ogres(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP,maxHP, appearance_msg)
        self._dmg = ((random.randint(2, 3)), 4)
   
    def attack1(self, player):
        print("The ogre swings his club.")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The ogre smashes your skull")
        player._hp -= self._dmg[1]

class BerserkerFairies(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP,maxHP, appearance_msg)
        self._dmg = ((random.randint(3, 4)), 5)
   
    def attack1(self, player):
        print("The fairy unleashes a spell")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The fairy spits fire")
        player._hp -= self._dmg[1]

class Pirates(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP,maxHP, appearance_msg)
        self._dmg = ((random.randint(4, 5)), 6)
   
    def attack1(self, player):
        print("The pirate swings his sword.")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The pirate stabs you.")
        player._hp -= self._dmg[1]



class Ghoul(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP,maxHP, appearance_msg)
        self._dmg = ((random.randint(6, 7)), 8)
   
    def attack1(self, player):
        print("The ghoul phases through you.")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The ghoul imbued a curse on you.")
        player._hp -= self._dmg[1]



class OgreCommander(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP,maxHP, appearance_msg)
        self._dmg = ((random.randint(7, 9)), 10)
   
    def attack1(self, player):
        print("The Commander swings his club.")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The Commander throw you into the wall.")
        player._hp -= self._dmg[1]


class BerserkerFairyMonarch(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP,maxHP, appearance_msg)
        self._dmg = ((random.randint(6, 8)), 9)
   
    def attack1(self, player):
        print("The Monarch unleashes a spell.")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The Monarch engulfs you in flames.")
        player._hp -= self._dmg[1]


class PirateKing(Enemy):
    def __init__(self, HP, maxHP, appearance_msg):
        super().__init__(HP,maxHP, appearance_msg)
        self._dmg = ((random.randint(8, 10)), (random.randint(11, 12)))
   
    def attack1(self, player):
        print("The Pirate King slices you with his cutlass")
        player._hp -= self._dmg[0]
    def attack2(self, player):
        print("The Pirate King crushes you with his aura.")
        player._hp -= self._dmg[1]



skeleton = Skeletons(10, 10, "A Skeleton ambushes you from behind!")
spider = Spiders(10, 10, "A Spider digs their fangs into your leg!")
ogres = Ogres(15, 15, "An Ogre charges towards you.")
berserkerfairies = BerserkerFairies(20, 20, "A Fairy whispers into your ear.")
pirates = Pirates(20, 20, "A Pirate swings his sword at you.")
# mini bosses
ghoul = Ghoul(30, 30, "An ominous aura engulfs you.")
# bosses
berserker_fairy_monarch = BerserkerFairyMonarch(30, 30, "A sinister smile stretches the Fairy Monarch's face as she plunges a knife into your chest.")
ogre_commander = OgreCommander(40, 40, "The Ogre Commander lets out a battle cry.")
pirate_king = PirateKing(60, 60, "The Pirate King ushes you to pick up your weapon for the final time.")

