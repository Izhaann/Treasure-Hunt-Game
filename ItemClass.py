class Item:
    def __init__(self, name, description):
        self.description = description
        self._name = name
    def get_description(self):
        print(self.description)
    def get_name(self):
        return (self._name)



class FairiesBlessing(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def use(self, player):
        player._maxStamina += 20



class OgresHeart(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def use(self, player):
        player._maxHP += 10



class Healing_item(Item):
    def __init__(self, name, heal, description):
        super().__init__(name, description)
        self._heal_amount = heal
    def use(self, player):
        if (player._maxHP - player._hp) < self._heal_amount:
            player.add_hp(player._maxHP - player._hp)
        else:
            player.add_hp(self._heal_amount)




class Stamina_item(Item):
    def __init__(self, name, stamina, description):
        super().__init__(name, description)
        self._stamina_amount = stamina
    def use(self, player):
        if (player._maxStamina - player._stamina) < self._stamina_amount:
            player.add_stamina(player._maxStamina - player._stamina)
        else:
            player.add_stamina(self._stamina_amount)



class Sleep_Potion(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def use(self, enemy):
        pass
        # This will spare the enemies turn, need to create the in battle/ battle state machine first.




class Steak_item(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def use(self, player):
        player._strength = True







                                                            #ITEMS



HealingPotion = Healing_item("Healing Potion", 15, " A Regular Healing Potion. Restores 15HP")
LargeHealingPotion = Healing_item("Large Healing Potion", 30, " A Large Healing Potion. Restores 30HP")
MaxHealingPotion = Healing_item("Max Healing Potion", 60, " A Max Healing Potion. Restores all of your HP")

StaminaPotion = Stamina_item("Stamina Potion", 15, " A Regular Stamina Potion. Restores 15 Stamina")
LargeStaminaPotion = Stamina_item("Large Stamina Potion", 30, " A Large Stamina Potion. Restores 30 Stamina")
MaxStaminaPotion = Stamina_item("Max Stamina Potion" ,60, " A Max Stamina Potion. Restores all of your Stamina")

Steak = Steak_item("Steak", "A delectable, juicy chunk of meat. Increases strength by 20%. Lasts for 3 turns.")


Ogres_Heart = OgresHeart("Ogre's Heart", "The heart of the Ogre Commander. Increases your max HP by 10 forever.")
Fairies_Blessing = FairiesBlessing("Fairies Blessing", "The Fairies final blessing. Increases your max Stamina by 20 forever")
