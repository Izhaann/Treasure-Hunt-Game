import random
import getch
from collections import deque
import os
import platform
from ChestClasses import chestDistributionWeights, WeightedChance, GetChestName
from WeaponClass import Weapon
from PlayerClass import Player
from PlayerInventoryClass import Bag
import questionary
from GameDevelopmentToolsFunctions import clear_console, TimerSleep
from CombatSystem import Combat
import time

import threading


clear_console()





class Maze:
    def __init__(self, player, enemy, mazeSize):
        self.player = player
        self.enemy = enemy
        self.mazeSize = mazeSize
        self.startX = 2*random.randint(0, self.mazeSize//2 - 1) + 1
        self.startY = 2*random.randint(0, self.mazeSize//2 - 1) + 1
        self.maze = self.Generate()
        self.min_distance = self.mazeSize//2
        self.exitX = None
        self.exitY = None
        self.errorcount = 0
        self.itemPos = []
        self.weaponPos = []
        self.enemyPos = []
        self.ChestStatus = [Player._currentLocation.GetChest(), Player._currentLocation.GetChest()]


    def CleanUp(self):
        self.maze = self.Generate()






    def Generate(self):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        maze = [[True]*self.mazeSize for x in range(self.mazeSize)]
        
        stack = [(self.startX, self.startY)]
        while len(stack) > 0:
            currentX, currentY = stack[-1]
            if (maze[currentY][currentX]):
                maze[currentY][currentX] = False
            random.shuffle(directions)
            
            neighbours = []
            
            for dir in directions:
                midX, midY = currentX + dir[0], currentY + dir[1]
                newX, newY = midX + dir[0], midY + dir[1]
                
                if 0 <= newX < self.mazeSize and 0 <= newY < self.mazeSize and maze[newY][newX] and maze[midY][midX]:
                    neighbours.append((newX, newY, midX, midY))

            if neighbours:
                newX, newY, midX, midY = random.choice(neighbours)
                maze[newY][newX] = False
                maze[midY][midX] = False
                stack.append((newX, newY))
            else:
                stack.pop()            
        return maze
    







    def ConvertCell(self, cell):
        if isinstance(cell, str):
            return cell
        elif cell: 
            return "☐" 
        else:
            return " "
    def PrintMaze(self, maze):
        final_maze = []
        for row in maze:
            converted_row = [self.ConvertCell(cell) for cell in row]
            final_maze.append(converted_row)
        for row in final_maze:
            print("  ".join(x for x in row))








    def GenerateEntities(self):
        possibleExits = []
        minDistance = self.mazeSize * 2
        
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
        queue = [(self.startX, self.startY)]
        distanceLevels = {}
        currentLevel = 0

        while queue:
            nextLevel = []
            for i in range(len(queue)):
                currentX, currentY = queue[i]
                if currentLevel > minDistance:
                    possibleExits.append((currentX, currentY))
                
                random.shuffle(directions)
                
                for dir in directions:
                    newX, newY = currentX + dir[0], currentY + dir[1]
                    
                    if 0 < newX < self.mazeSize and 0 < newY < self.mazeSize and not self.maze[newY][newX]:
                        if (newX, newY) not in distanceLevels:
                            distanceLevels[(newX, newY)] = currentLevel + 1
                            nextLevel.append((newX, newY))
            
            queue = nextLevel
            currentLevel += 1

        self.enemyPos = [possibleExits[random.randint(0, len(possibleExits) - 1)], possibleExits[random.randint(0, len(possibleExits) - 1)]]



        possibleExits = [exit for exit in possibleExits if sum(
            1 for dir in directions if 0 <= exit[1] + dir[1] < self.mazeSize and 0 <= exit[0] + dir[0] < self.mazeSize and 
            self.maze[exit[1] + dir[1]][exit[0] + dir[0]]
        ) >= 3]

                

        if (len(possibleExits) < 3):
            self.CleanUp()
            self.GenerateEntities()
            return
         
        (self.exitX, self.exitY) = (possibleExits[random.randint(0, len(possibleExits) - 1)])
        possibleExits.remove((self.exitX, self.exitY))



        self.itemPos = [possibleExits[random.randint(0, len(possibleExits) - 1)]]
        possibleExits.remove(self.itemPos[0])
        self.itemPos.append(possibleExits[random.randint(0, len(possibleExits) - 1)])     
        
        if Player._currentLocation.weapon != None:
            if random.randint(1, 5) == 5:
                self.weaponPos.append(possibleExits[random.randint(0, len(possibleExits) - 1)])





    
    def PlayerExplore(self):
        item1NotFound = True
        item2NotFound = True
        Enemy1NotEncountered = True
        Enemy2NotEncountered = True
        self.GenerateEntities()
        playerX, playerY = self.startX, self.startY
        def IsValidMove(maze, positionX, positionY):
            print((positionX, positionY))
            return 0 < positionX < self.mazeSize and 0 < positionY < self.mazeSize and not maze[positionY][positionX] or isinstance(maze[positionY][positionX], str)
        

                                                                 # Adding The Items into the map
        self.maze[self.startY][self.startX] = "⍥"
        self.maze[self.exitY][self.exitX] = "E"
        if self.weaponPos:
            self.maze[self.weaponPos[0][1]][self.weaponPos[0][0]] = "W"
            

        for idx, pos in enumerate(self.itemPos):
            x, y = pos
            chestIndex = self.ChestStatus[idx]
            
    
            if chestIndex == 0:
                self.maze[y][x] = "B"  
            elif chestIndex == 1:
                self.maze[y][x] = "S" 
            elif chestIndex == 2:
                self.maze[y][x] = "G"  

                                                                    # Player controls

        while True:
            clear_console()
            self.PrintMaze(self.maze)
            PlayerInput = getch.getch()
            if PlayerInput.lower() == "w":
                if IsValidMove(self.maze, playerX, playerY-1):
                    self.maze[playerY][playerX] = False
                    playerY = playerY-1
                    self.maze[playerY][playerX] = "⍥"
                    clear_console()
                    self.PrintMaze(self.maze)
            elif PlayerInput.lower() == "a":
                if IsValidMove(self.maze, playerX-1, playerY):
                    self.maze[playerY][playerX] = False
                    playerX = playerX-1
                    self.maze[playerY][playerX] = "⍥"
                    clear_console()
                    self.PrintMaze(self.maze)
                
            elif PlayerInput.lower() == "s":
                if IsValidMove(self.maze, playerX, playerY+1):
                    self.maze[playerY][playerX] = False
                    playerY = playerY+1
                    self.maze[playerY][playerX] = "⍥"
                    clear_console()
                    self.PrintMaze(self.maze)
                
            elif PlayerInput.lower() == "d":
                if IsValidMove(self.maze, playerX+1, playerY):
                    self.maze[playerY][playerX] = False
                    playerX= playerX+1
                    self.maze[playerY][playerX] = "⍥"
                    clear_console()
                    self.PrintMaze(self.maze)

            
            if self.itemPos:
                if (playerX, playerY) == (self.itemPos[0][0], self.itemPos[0][1]) and item1NotFound:
                        item1NotFound = False
                        input(f"You found a {GetChestName(self.ChestStatus[0])}!")
                        item1 = Player._currentLocation.GetItem(self.ChestStatus[0])
                        input(f"Inside was a {item1.get_name()}")
                        ItemStoreChoice = questionary.select(
                                "What do you want to do?",
                                choices=[
                                    'Take it',
                                    'Leave it',
                                ]).ask()
                        if ItemStoreChoice == 'Take it':
                             Bag.Store(item1)
                             input(Bag.OpenBag())
                        
                
                
                if (playerX, playerY) == (self.itemPos[1][0], self.itemPos[1][1]) and item2NotFound:
                        item2NotFound = False
                        input(f"You found a {GetChestName(self.ChestStatus[1])}!")
                        item2 = Player._currentLocation.GetItem(self.ChestStatus[0])
                        input(f"Inside was a {item2.get_name()}")
                        ItemStoreChoice = questionary.select(
                                "What do you want to do?",
                                choices=[
                                    'Take it',
                                    'Leave it',
                                ]).ask()
                        if ItemStoreChoice == 'Take it':
                             Bag.Store(item2)
                             input(Bag.OpenBag())
                        
                             

            if self.weaponPos:
                if (playerX, playerY) == (self.weaponPos[0][0], self.weaponPos[0][1]):
                            input(f"You found a {Player._currentLocation.weapon.get_name()}!")
                            self.weaponPos.remove(self.weaponPos[0])
                            ItemStoreChoice = questionary.select(
                                "What do you want to do?",
                                choices=[
                                    'Take it',
                                    'Leave it',
                                ]).ask()
                            if ItemStoreChoice == 'Take it':
                             Bag.Store(Player._currentLocation.weapon)
                             input(Bag.OpenArsenal())



            if (playerX, playerY) == (self.enemyPos[0][0], self.enemyPos[0][1]) and Enemy1NotEncountered:
                        Enemy1NotEncountered = False
                        input(Player._currentLocation._enemies.appearance_msg())
                        print("Prepare for combat")
                        TimerSleep()
                        Combat.ResetEnemy(Player._currentLocation._enemies)
                        Combat.CombatMenu(Player._currentLocation._enemies)
                        
            if (playerX, playerY) == (self.enemyPos[1][0], self.enemyPos[1][1]) and Enemy2NotEncountered:
                        Enemy2NotEncountered = False
                        input(Player._currentLocation._enemies.appearance_msg())
                        print("Prepare for combat")
                        TimerSleep()
                        Combat.ResetEnemy(Player._currentLocation._enemies)
                        Combat.CombatMenu(Player._currentLocation._enemies)



            if (playerX, playerY) == (self.exitX, self.exitY):
                print("Well done! You have completed the maze!")
                break

def CreateMaze():
    
    maze = Maze(2, 2, 17)
    maze.PlayerExplore()
    





def ActionPrompt():
    
    def prompt_with_sleep():
        RoomCount = 1
        Action = questionary.select(
            "What will you do?",
            choices = [
                "Explore",
                "Check Inventory",
            ]
        ).ask()

        if Action == "Explore":
            CreateMaze()
            RoomCount += 1
            if RoomCount <= 4:
                prompt_with_sleep()

            else:
                 return ""

        if Action == "Check Inventory":
            Bag.OpenInventory()
            prompt_with_sleep()

    prompt_thread = threading.Thread(target=prompt_with_sleep)
    prompt_thread.start()
    prompt_thread.join()
    


    

