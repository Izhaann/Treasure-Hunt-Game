from LocationClasses import GetLocationDescription, Write, WriteCustomTime, GodValley, GhastlyReef, SkullyWagShores, VenomousCove, WhisperingHollow, Brutalith, BlackWater
from PlayerClass import Player
import questionary
from colorama import init, Fore, Style
from art import text2art
import pyfiglet
from PlayerInventoryClass import Bag
import getch
from MazeGeneration import CreateMaze, ActionPrompt
init()

    
    



def EnterIsland(Island):
    GetLocationDescription(Island)
    Player._currentLocation = Island
    

def StartGame():
    GetLocationDescription("Start")
    Player.name = input("My name is: ")
    print(f"\n\n\033[1m\033[33m???: \033[0m")
    Write(f"Hello {Player.name}, nice to meet you!")
    Write(f" Anyways enough of the introduction, it looks like we are heading to our first island.")


def TitleScreen():
    title_ascii_ar = text2art("HUNT", font="ghost")
    title_ascii_art = Fore.RED + title_ascii_ar + Style.RESET_ALL
    print(title_ascii_art)
    TitleScreenSelection = questionary.select(
        "Choose an action.",
        choices = [
            "Start Game",
            "How to Play",
            "Exit"
    ]).ask()
    if TitleScreenSelection == "Start Game":
        MainLoop()
    elif TitleScreenSelection == "How to Play":
        print("The gameplay focusses mainly on a character who navigates their way through mazes.")
        print("\n\033[4mControls:\033[0m")
        print("\033[1mMaze Controls:\033[0m simply press (W, A, S, D)")
        print("\033[1mSelection Controls:\033[0m Arrow keys to move, Enter to select")
        print("\n\033[4mInfo:\033[0m")
        print("\033[1mB, S, G =\033[0mBronze, Silver, Gold Chest")
        print("\033[1mE =\033[0m Exit")
        print("\033[1mW = \033[0mWeapon")
    return ""


def MainLoop():
    StartGame()
    NextIsland = questionary.select(
        "Which island will you sail to?",
        choices = [
            "Skully Wag Shores",
            
        ]).ask()
    if NextIsland == "Skully Wag Shores":
        EnterIsland(SkullyWagShores)
        ActionPrompt()
        
    



    NextIsland = questionary.select(
        "Which island will you sail to?",
        choices = [
            "Venomous Cove",
            "Ghastly Reef"

            
        ]).ask()
    if NextIsland == "Venomous Cove":
        EnterIsland(VenomousCove)
        ActionPrompt()
        NextIsland = questionary.select(
        "Which island will you sail to?",
        choices = [
            "Ghastly Reef",

        ]).ask()
        if NextIsland == "Ghastly Reef":
            EnterIsland(GhastlyReef)
            ActionPrompt()
    elif NextIsland == "GhastlyReef":
        EnterIsland(GhastlyReef)
        ActionPrompt()







    NextIsland = questionary.select(
        "Which island will you sail to?",
        choices = [
            "Whispering Hollow",

        ]).ask()
    if NextIsland == "Whispering Hollow":
        EnterIsland(WhisperingHollow)
        ActionPrompt()



    NextIsland = questionary.select(
            "Which island will you sail to?",
            choices = [
                "Brutalith",
                "BlackWater Bay"
            ]).ask()
    if NextIsland == "Brutalith":
        EnterIsland(Brutalith)
        ActionPrompt()
        NextIsland = questionary.select(
            "Which island will you sail to?",
            choices = [
                "BlackWater Bay"
            ]).ask()
        if NextIsland == "BlackWater Bay":
            EnterIsland(BlackWater)
            ActionPrompt()
    
    elif NextIsland == "BlackWater Bay":
        EnterIsland(BlackWater)
        ActionPrompt()
    

    NextIsland = questionary.select(
            "Which island will you sail to?",
            choices = [
                "God Valley"
            ]).ask()
    if NextIsland == "God Valley":
            EnterIsland(GodValley)
            ActionPrompt()
            GetLocationDescription("Ending")
    

        
        
        

    
    




    
    


        
    



TitleScreen()
