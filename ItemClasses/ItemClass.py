from PlayerClass import Player
class Item:
    def __init__(self, description):
        self.description = description
    def get_description(self):
        print(self.description)


class Healing_item(Item):
    def __init__(self, heal, description):
        super().__init__(description)
        self._heal_amount = heal
    def use(self, player):
        player._hp += self._heal_amount

HealingPotion = Healing_item(15, " A Regular Healing Potion. Heals for 15HP")
LargeHealingPotion = Healing_item(30, " A Large Healing Potion. Heals for 30HP")
MaxHealingPotion = Healing_item(60, " A Max Healing Potion. Heals for your max HP")

class Stamina_item(Item):
    def __init__(self, stamina, description):
        super().__init__(description)
        self._stamina_amount = stamina
    def use(self, player):
        player._stamina += self._stamina_amount
    
HealingPotion.use(Player)
