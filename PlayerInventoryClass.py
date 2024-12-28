from ItemClass import HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, Steak, OgresHeart, FairiesBlessing
from WeaponClass import cutlass, mace, scythe, club, katana
from PlayerClass import Player
import questionary
from GameDevelopmentFunctionTools import clear_console

class Inventory():
    def __init__(self, capacityMax):
        
        self.items = {
            HealingPotion: 10,
            LargeHealingPotion: 0,
            MaxHealingPotion: 0,
            StaminaPotion: 0,
            LargeStaminaPotion: 0,
            MaxStaminaPotion: 0,
            Steak: 0,
            OgresHeart: 0,
            FairiesBlessing: 0


        }
        self.weapons = {
            cutlass: 0, 
            mace: 0, 
            scythe: 0, 
            club: 0, 
            katana: 0
        }
        self._capacityMax = capacityMax
        self._capacity = sum(self.items.values())


    def GetCurrentWeapons(self):
        array = []  
        for weapon, count in self.weapons.items():  
            if count != 0:  
                array.append(str(count))
        return array





    def CapacityCheck(self):
        if self._capacity >= self._capacityMax:
            print("Your Bag is too full.")
            DropItemTrueorFalse = questionary.select(
                "Would you like to drop an item?",
                choices = [
                    "Yes",
                    "No"
                ]).ask()
            if DropItemTrueorFalse == "Yes":
                self.Drop()
                return True
            return False
        return True
                





    def OpenBag(self):
        print("Here are your stored items (Type Drop to drop an item):")
        for item in self.items:
            if self.items.get(item) != 0:
                print(f"{item.get_name()} x{self.items.get(item)} |  {item.get_description()}")

        if input().lower() == "drop":
            self.Drop()

        return ""
        
    


    def Drop(self):
        clear_console()
        item_name_to_instance = {item.get_name(): item for item in self.items if self.items[item] != 0}
        DropItemChoice = questionary.select(
            "What do you want to drop?",
            choices=list(item_name_to_instance.keys())
        ).ask()
        
        selected_item_instance = item_name_to_instance[DropItemChoice]
        
        self.Remove(selected_item_instance)
        self.OpenBag()




    def OpenArsenal(self):
        for weapon in self.weapons:
            if self.weapons.get(weapon) != 0:
                if weapon == Player.current_weapon:
                    print(f"{weapon.get_name()} | {weapon.get_desc()} - CURRENT WEAPON")
                else:
                    print(f"{weapon.get_name()} | {weapon.get_desc()}")
        input()
        clear_console()
        return ""


    def Store(self, item):
        if self.CapacityCheck():
                if item in self.items:
                    self.items[item] += 1
                elif item in self.weapons:
                    self.weapons[item] += 1

    def Remove(self, item):
        self.items[item] -= 1

    
    
 








    def OpenInventory(self):
        clear_console()
        InventoryChoice = questionary.select(
                "What do you want to do?",
                choices=[

                    'Show Items',
                    'Show Weapons',
                    'Equip Weapon',

                ]).ask()
        if InventoryChoice == 'Show Items':
            self.OpenBag()
            return self.OpenInventory()
        elif InventoryChoice == 'Show Weapons':
            self.OpenArsenal()
            return self.OpenInventory()
        elif InventoryChoice == 'Equip Weapon':
            WeaponEquipChoice = questionary.select(
                "What do you want to equip?",
                choices = [(weapon.get_name() for weapon in self.weapons if self.weapons[weapon] != 0)
                ]).ask()
            clear_console()
            input(f"You have equipped the {WeaponEquipChoice}")
            Player.equip(eval(WeaponEquipChoice.lower()))
            return self.OpenInventory()
    








Bag = Inventory(10)
