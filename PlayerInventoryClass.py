from ItemClass import HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, Steak, Ogres_Heart, Fairies_Blessing
class Inventory():
    def __init__(self, capacity):
        self._capacity = capacity
        self.items = {
        }

    def CapcatityCheck(self):
        if self

    def OpenBag(self):
        for item in self.items:
            print(f"{item.get_name()} x{self.items.get(item)} |  {item.get_description()}")
        return
    def Store(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def Remove(self, item):
        self._capacity -= 1
        self.items[item] -= 1


Bag = Inventory(10)