import random
mazeSize = 17

maze = [[True]*mazeSize for x in range(mazeSize)]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def PrintMaze():
    for row in maze:
        print("".join(["N" if x else " " for x in row]))
        
def GenerateMaze():
    startX, startY = 2*random.randint(0, mazeSize//2 - 1) + 1, 2*random.randint(0, mazeSize//2 - 1) + 1
        
    stack = [(startX, startY)]
    while len(stack) > 0:
        currentX, currentY = stack[-1]
        if (maze[currentY][currentX]):
            maze[currentY][currentX] = False
        random.shuffle(directions)
        
        neighbours = []
        
        for dir in directions:
            midX, midY = currentX + dir[0], currentY + dir[1]
            newX, newY = midX + dir[0], midY + dir[1]
            
            if 0 <= newX < mazeSize and 0 <= newY < mazeSize and maze[newY][newX] and maze[midY][midX]:
              neighbours.append((newX, newY, midX, midY))

        if neighbours:
            newX, newY, midX, midY = random.choice(neighbours)
            maze[newY][newX] = False
            maze[midY][midX] = False
            stack.append((newX, newY))
        else:
            stack.pop()              
    
GenerateMaze()
PrintMaze()