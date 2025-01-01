from ItemClass import HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, Steak, OgresHeart, FairiesBlessing
from WeaponClass import stick, cutlass, mace, scythe, club, katana
from PlayerClass import Player
import questionary
from GameDevelopmentToolsFunctions import clear_console, TimerSleep
class Inventory():
    def __init__(self, capacityMax):
        
        self.items = {
            HealingPotion: 0,
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
            stick: 1,
            cutlass: 0, 
            mace: 0, 
            scythe: 0, 
            club: 0, 
            katana: 0
        }
        self._capacityMax = capacityMax
        self._capacity = 0


    def GetCurrentWeapons(self):
        array = []  
        for weapon, count in self.weapons.items():  
            if count != 0:  
                array.append(str(count))
        return array





    def CapacityCheck(self):

        if self._capacity < self._capacityMax:
            return True
        else:
            return False
                





    def OpenBag(self):

        if self._capacity == 0:
            input("You do not currently own any Items..")
            return ""
        
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
        return ""


    def Store(self, item):
        if self.CapacityCheck():
                if item in self.items:
                    self.items[item] += 1
                    self._capacity += 1
                elif item in self.weapons:
                    self.weapons[item] += 1
        else:
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

            if DropItemTrueorFalse == 'No':
                return False

    def Remove(self, item):
        self.items[item] -= 1
        self._capacity -= 1

    
    
 








    def OpenInventory(self):
        clear_console()
        InventoryChoice = questionary.select(
                "What do you want to do?",
                choices=[

                    'Show Items',
                    'Use Item',
                    'Show Weapons',
                    'Equip Weapon',
                    'Back',

                ]).ask()
        if InventoryChoice == 'Show Items':
            self.OpenBag()
            return self.OpenInventory()
        

        elif InventoryChoice == 'Use Item':
            if self._capacity ==0:
                input("You have no items to use :(")
                return ""

            choices = [item.get_name() for item in self.items if self.items[item] != 0]
            choices.append("Back")
            UseItemChoice = questionary.select(
                "Which item would you like to use?",
                choices = choices
                ).ask()
            if UseItemChoice == 'Back':
                return self.OpenInventory()
            self.UseItem(eval("".join(UseItemChoice.split(" "))))
            print(f"You used a {UseItemChoice}")
            TimerSleep()
                
            
        
        
        elif InventoryChoice == 'Show Weapons':
            self.OpenArsenal()
            return self.OpenInventory()

            
        elif InventoryChoice == 'Equip Weapon':
            choices = [weapon.get_name() for weapon in self.weapons if self.weapons[weapon] != 0]
            choices.append("Back")
            WeaponEquipChoice = questionary.select(
                "What do you want to equip?",
                choices = choices
                    ).ask()
            if WeaponEquipChoice == 'Back':
                return self.OpenInventory()
            
            clear_console()
            input(f"You have equipped the {WeaponEquipChoice}")
            Player.equip(eval(WeaponEquipChoice.lower()))
            return self.OpenInventory()

        elif InventoryChoice == 'Back':
            return ""
        
    
    def UseItem(self, item):
        item.use(Player)
        self.items[item] -= 1
        self._capacity -= 1
        
    








Bag = Inventory(10)
#Bag.OpenInventory()
