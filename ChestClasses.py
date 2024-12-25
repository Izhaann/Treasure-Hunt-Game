from ItemClass import HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, Steak
import random
ItemAssignment = [HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, Steak]



chestDistributionWeights = [
    # HP  LHP MHP SP LSP MSP S
    [30, 15, 0, 30, 15, 0, 10], # Wooden
    [20, 15, 10, 20, 15, 10, 10], # Silver
    [15, 10, 25, 15, 10, 25, 20], # Golden
]

def WeightedChance(weights):
    sumOfWeights = sum(weights)
    chance = random.randint(0, sumOfWeights - 1)
    weighted = 0
    for i, x in enumerate(weights):
        weighted += x
        if chance < weighted:
            return i
print(ItemAssignment[WeightedChance(chestDistributionWeights[0])].get_description())

def GetChestName(Index):
    if Index == 0:
        return "Bronze Chest"
    if Index == 1:
        return "Silver Chest"
    if Index == 2:
        return "Gold Chest"