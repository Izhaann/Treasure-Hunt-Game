from WeaponClass import cutlass, mace, katana, scythe, club
from EnemiesClass import skeleton, spider, ogres, pirates, berserkerfairies, pirate_king
from ItemClass import HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, Steak, OgresHeart, FairiesBlessing
from ExplorationStateMachine import PlayerExplorationStateMachine
from ChestClasses import chestDistributionWeights, WeightedChance, ItemAssignment



class Location(PlayerExplorationStateMachine):
    def __init__(self, chest_probability, enemies, weapon):
        
        self._enemies = enemies
        self._chest_probability = chest_probability
        self.weapon = weapon

    def GetChest(self):
        return (WeightedChance(self._chest_probability))
    def GetItem(self, chestIndex):
        return ItemAssignment[WeightedChance(chestDistributionWeights[chestIndex])]
        
        
    

    def EnterRoom(self):
        pass
        #room.enemy shuffle
        #room. chest shuffle
    def GetDesc(self):
        print("description goes here")

    def GetDesc(self):
        input("description for skull island goes here")









SkullyWagShores = Location((80, 15, 5), skeleton, cutlass)


print(SkullyWagShores.GetItem(SkullyWagShores.GetChest()).get_name())
SkullyWagShores.EnterRoom()