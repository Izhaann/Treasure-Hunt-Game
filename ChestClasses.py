from ItemClass import HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, SleepPotion
import random
ItemAssignment = [HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, SleepPotion]



chestDistributionWeights = [
    # HP  LHP MHP SP LSP MSP S
    [40, 15, 5, 20, 15, 0, 5], # Wooden
    [20, 20, 15, 20, 10, 5, 10], # Silver
    [15, 20, 30, 15, 15, 15, 20], # Golden
]

def WeightedChance(weights):
    sumOfWeights = sum(weights)
    chance = random.randint(0, sumOfWeights - 1)
    weighted = 0
    for i, x in enumerate(weights):
        weighted += x
        if chance < weighted:
            return i

def GetChestName(Index):
    if Index == 0:
        return "Bronze Chest"
    if Index == 1:
        return "Silver Chest"
    if Index == 2:
        return "Gold Chest"