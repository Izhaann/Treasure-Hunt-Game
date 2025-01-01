from WeaponClass import cutlass, mace, katana, scythe, club
from EnemiesClass import skeleton, spider, ogres, pirates, elves, pirate_king, ghoul, ogre_commander, elf_monarch
from ItemClass import HealingPotion, LargeHealingPotion, MaxHealingPotion, StaminaPotion, LargeStaminaPotion, MaxStaminaPotion, Steak, OgresHeart, FairiesBlessing
from ExplorationStateMachine import PlayerExplorationStateMachine
from ChestClasses import chestDistributionWeights, WeightedChance, ItemAssignment
import time
from GameDevelopmentToolsFunctions import clear_console
from rich import print
import sys
import getch


class Location(PlayerExplorationStateMachine):
    def __init__(self, chest_probability, enemies, weapon):
        
        self._enemies = enemies
        self._chest_probability = chest_probability
        self.weapon = weapon

    def GetChest(self):
        return (WeightedChance(self._chest_probability))
    def GetItem(self, chestIndex):
        return ItemAssignment[WeightedChance(chestDistributionWeights[chestIndex])]
        
        
    def GetDesc(self):
        print("description goes here")










SkullyWagShores = Location((80, 15, 5), skeleton, cutlass)
VenomousCove = Location((70, 35, 5), spider, mace)
GhastlyReef = Location((60, 30, 10), ghoul, scythe)
WhisperingHollow = Location((50, 30, 20), elves, katana) # + elf monarch

Brutalith = Location((50, 25, 25), ogres, club) # + ogre commander
BlackWater = Location((40, 25, 35), pirates, None)
# just the bossfight
GodValley = Location((0, 0, 0), pirate_king, None)

def Write(Sentence):
    for char in Sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def WriteCustomTime(Sentence, Time):
    for char in Sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(Time)
        







def GetLocationDescription(Location):
    

    if Location == "Start":
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("Flooding with confidence and with your trusty weapon:\033[1m the Stick\033[0m you unleash your boat from it's dock, bidding farewell to the comfort of your familiar home and sailing into the darkness of the unknown.")
        Write("\nMany miles from home, a sudden rattling from a barrel catches your attention.")
        Write("\nAs you go to investigate this strange phenomenon, a flying elf springs out.")

        print(f"\n\n[bold yellow]???: [/bold yellow]")
        Write("Hello, my name is"), print(f" [bold yellow]Puck[/bold yellow]."), Write("I heard you were travelling to God Valley, you must be an idiot!")
        Write("\nI have some business I need to take care of on the way there so I thought I would help myself in tagging along. You are welcome.")
        Write("\nThats enough about me, what is your name?")

        Write("\n\nReluctant to converse with such an annoying creature, you fight the urge to squash it as you give your name.")

        print(f"\n\n[bold green]???: [/bold green]")
        return ""
    if Location == SkullyWagShores:
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("\033[32mSkully Wag Shores\033[0m\n")
        Write("\n*Desparity engulfed the place around you. Everything in your sight had this eerie feeling of emptiness and abandonment.")
        Write("\nThe once vibrant landscape now lay in a haunting silence, as if the world itself had been drained of life.")
        Write("\nThe skies above, once filled with the hues of dawn, were now a dull, oppressive gray, heavy with the weight of forgotten memories.")
        Write("\nThe ground beneath your feet seemed lifeless, cracked and parched, as though it had long since ceased to care for the passage of time... *")

        print(f"\n\n[bold yellow]Puck: [/bold yellow]")
        
        Write("Welcome to Skully Wag Shores.")
        Write("\nThe remnants of a disaster-struck island. This place was the first to be corrupted by \033[31mThe Pirate King's\033[0m  greed.")
        Write("\nAll life on this island died years ago, the only spur of hope for this land lying in the souls of the skeletons that walk it.")
        Write("\nThis is the first obstacle for those trying to reach God Valley, and for some its their last. Tread carefully.")
        input()
    if Location == VenomousCove:
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("\033[32mVenomous Cove\033[0m\n")
        Write("*Trails of webs shroud the terrain infront of you. The tangled forest ahead tainted with towering arachnids that crawled through the labyrinth of webs...*")

        print(f"\n\n[bold yellow]Puck: [/bold yellow]")

        Write("I always hated spiders.")
        Write("\nThey say this place used to be a tropical island that acted as a safe haven to wonderous travellers.")
        Write("\nAfter \033[31m The King\033[0m claimed this place as his own, he experimented on the insects to raise mindless soldiers.")
        Write("\nHow tragic.")
        input()
        return ""
    if Location == GhastlyReef:
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("\033[32mGhastly Reef\033[0m\n")
        Write("*Hows echoed through the land as gusts of wind blew icy cold air. Rotting plant-life littered the land, standing beneath the eerily dark hues of the sky.")
        Write("There was not a soul in sight, yet it seemed as though your every move was being observed. A barren wasteland, silently withering away in the corner of the Earth awaited you...*")

        print(f"\n\n[bold yellow]Puck: [/bold yellow]")
        Write("This place is creepy. I have an unshakeable feeling that we're being watched.")
        Write("Even being the amazing, smart, intelligent, unrivaled dictionary I am, I have never heard much of this place.")
        Write("One thing is for sure though: we aren't alone.")
        input()
        return ""

    if Location == WhisperingHollow:
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("\033[32mWhispering Hollow\033[0m\n")
        Write("*A paradise could be the only words to describe this haven.")
        Write("\nFireflies playfully danced in the luscious trees that seemed as old as time itself.")
        Write("\nIn the heart of this enchanted woodland, a crystal-clear stream winds its way through the underbrush, its waters glowing with a soft blue light as if infused with magic...*")

        print(f"\n\n[bold yellow]Puck: [/bold yellow]")
        Write("This is it. My home town.")
        Write("\nDon't be fooled by its mystical exterior. This place is the most evil one that you will encounter.")
        Write("\nThe real reason I had come with you on this journey was because I wanted you to help me save this place.")
        Write("\nSeeing your strength up until now, I know that you can do it.")
        Write("\nThe Monarch has been corrupted by \033[31mThe Pirate King\033[0m. Now blinded by money and power, the entire island only knows how to slaughter.")
        Write("\nMy companions, they may seem childish and playful, but they're truly evil. Be careful.")
        input()
        return ""
    if Location == "WhisperingHollowBossFight":
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("*The Elf Monarch gracefully sat on her throne, gazing down at you in arrogance.")

        print(f"\n\n[bold yellow]The Elf Monarch: [/bold yellow]")
        Write("\nI know what it's like to be blinded by rage and revenge. I can see it in your eyes, your actions speak violence yet your soul begs for peace.")
        Write("\nThere is no reason for us to fight, take it easy, you will be safe here with us forever...")

        Write("*Enchanted by her words you loosen the grip on your weapon. In some kind of daze, you lower your guard.*")
        elf_monarch.appearance_msg()

        return ""
    if Location == Brutalith:
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("\033[32mBrutalith\033[0m\n")
        Write("Overwhelmingly great statues greet you at the entrance of this land. Around you, Ogres battled each other as crowds cheered in delight.")
        Write("The terrain was littered with wild forests and enormous, crumbling stone ruins that whisper of ancient, monstrous inhabitants...*")

        print(f"\n\n[bold yellow]Puck: [/bold yellow]")
        Write("You thought you could get rid of me that easily?")
        Write("\nI wont wanna miss the final fight!")
        Write("\nMany legends have come from this place. The land of the most courageous that is ruled by SogeKing: the bravest warrior in the lands.")
        Write("\nThis is one of the only civilizations to not have been corrupted by \033[31mThe Pirate King\033[0m due to his immense respect for the place.")
        Write("\nWhy are we here then? To see if you are really worthy to defeat that corrupt ruler.")
        Write("\nDefeat the Ogre Commander and you will be ready for the final battle.")
        input()
        return ""

    if Location == "BrutalithBossFight":
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        print(f"\n\n[bold yellow]Ogre Commander: [/bold yellow]")
        Write("So you were the one who was able to defeat my strongest warriors. I commend your strengths, little one.")
        Write("\nProve to me your efforts to get here were not in vain, fight me with all your will.")
        ogre_commander.appearance_msg()
        return ""

    if Location == BlackWater:
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("\033[32mBlackWater Bay\033[0m\n")
        print(f"\n\n[bold yellow]Puck: [/bold yellow]")
        Write("This is the last stop in our reach \033[31mPThe Pirate King\033[0m.")
        Write("\nThis island was built almost like an iron-curtain to prevent anyone from progressing further.")
        Write("\nHis crew will be the toughest opponents you have ever faced.")
        Write("\nGood Luck.")
        input()
        return ""
    if Location == GodValley:
        clear_console()
        Skip=input("Skip Cutscene? (Y/N)")
        if Skip.lower() == "y":
            return ""
        Write("\033[32mGod Valley\033[0m\n")
        Write("*You final foe now sat infront of you, his great sword plunged into the ground beside him*")

        Write("\n\n\033[31mPirate King: \033[0m")
        Write("\nI have been expecting you.")
        Write("\nYou were the first ever to reach me, let me know your name.")
        # Nuts gives his name
        Write("\nNot very talkative I see.")
        Write("\nWell, not that there is any point, soon one of us will be slaughtered in the hands of the other.")
        Write("\nBe the one who can finally put my tyranny to an end.")
        input()
        pirate_king.appearance_msg()
        return ""
    if Location == "Ending":
        clear_console()
        print(f"\n\n[bold yellow]Pirate King: [/bold yellow]")
        WriteCustomTime("I have been bested...", 0.07)
        WriteCustomTime("\nDid you really think I kept all my treasure here?", 0.08)
        WriteCustomTime("\nYou want my treasure? You can have it.", 0.09)
        WriteCustomTime("\nI left everything I gathered together in one place.", 0.12)
        WriteCustomTime("\nNow you just have to find it...", 0.18)
        return ""
    




