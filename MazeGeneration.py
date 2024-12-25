import random
import getch
from collections import deque
import os
import platform
from ChestClasses import chestDistributionWeights, WeightedChance, GetChestName
from PlayerClass import Player

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  

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
        visited = [(self.startX, self.startY)]
        possibleExits = []
        minDistance = self.mazeSize * 1
        
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
        stack = [((self.startX, self.startY), 0)]
        while stack:
            (currentX, currentY), dist = stack.pop(0)
            if dist > minDistance:
                possibleExits.append((currentX, currentY))

            random.shuffle(directions)
            

            
            for dir in directions:
                newX, newY = currentX + dir[0], currentY + dir[1]
                
                if 0 <  newX < self.mazeSize and 0 < newY < self.mazeSize and not self.maze[newY][newX]:
                    if (newX, newY) not in visited:
                        visited.append((newX, newY))
                        stack.append(((newX, newY), dist+1))

        print(possibleExits)
        possibleExits = [exit for exit in possibleExits if sum(
            1 for dir in directions if self.maze[tuple(map(sum, zip(exit, dir)))[1]][tuple(map(sum, zip(exit, dir)))[0]]
        ) >= 3]
                
         
        (self.exitX, self.exitY) = (possibleExits[random.randint(0, len(possibleExits) - 1)])
        possibleExits.remove((self.exitX, self.exitY))



        self.itemPos = [possibleExits[random.randint(0, len(possibleExits) - 1)]]
        possibleExits.remove(self.itemPos[0])
        self.itemPos.append(possibleExits[random.randint(0, len(possibleExits) - 1)])                    

        return self.exitX, self.exitY
        





    
    def PlayerExplore(self):
        self.exitX, self.exitY = self.GenerateEntities()
        playerX, playerY = self.startX, self.startY
        def IsValidMove(maze, positionX, positionY):
            print((positionX, positionY))
            return 0 < positionX < self.mazeSize and 0 < positionY < self.mazeSize and not maze[positionY][positionX] or isinstance(maze[positionY][positionX], str)
        

                                                                    # Adding The Items into the map
        self.maze[self.startY][self.startX] = "⍥"
        self.maze[self.exitY][self.exitX] = "E"

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
                if (playerX, playerY) == (self.itemPos[0][0], self.itemPos[0][1]):
                    input(f"You found a {GetChestName(self.ChestStatus[0])}!")
                    input(f"Inside was a {Player._currentLocation.GetItem(self.ChestStatus[0]).get_name()}")
                    self.itemPos.remove(self.itemPos[0])
                    self.ChestStatus.remove(self.ChestStatus[0])


            if (playerX, playerY) == (self.exitX, self.exitY):
                print("Well done! You have completed the maze!")
                break


maze = Maze(2, 2, 7)            
mazeGenerate = maze.Generate()
maze.PlayerExplore()
print(maze.GenerateEntities())
