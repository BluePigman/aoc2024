import time


f = open("day6.txt")

start_time = time.time()

# turn text file into a 2d grid

grid = [line.rstrip() for line in f.readlines()]

M = len(grid)
N = len(grid[0])

# find start position
startY, startX = 0, 0
for i in range(M):
    for j in range(N):
        if grid[i][j] == "^":
            startY = i
            startX = j
            break

def part1():

    posY, posX = startY, startX
    # move guard and count unique squares

    visited = set()
    dir = 0
    delta = [-1, 0, 1, 0, -1]
    while posY < M and posX < N:
        deltaY = delta[dir]
        deltaX = delta[dir + 1]

        if posY + deltaY == M or posX + deltaX == N or posY + deltaY == -1 or posX + deltaX == -1: # exit
            break

        if grid[posY + deltaY][posX + deltaX] == "#": # obstacle
            dir = (dir + 1) % 4

        else: # move
            posY += deltaY
            posX += deltaX
            visited.add((posY, posX))
    print(len(visited))


def part2():
    # brute force - for every coordinate put an obstacle and test if a loop will occur
    
    def isLoop():
        visited = set()
        dir = 0
        delta = [-1, 0, 1, 0, -1]
        posY, posX = startY, startX
        while posY < M and posX < N:
            deltaY = delta[dir]
            deltaX = delta[dir + 1]

            if posY + deltaY == M or posX + deltaX == N or posY + deltaY == -1 or posX + deltaX == -1: # exit
                return False

            if grid[posY + deltaY][posX + deltaX] == "#": # obstacle
                dir = (dir + 1) % 4

            else: # move
                posY += deltaY
                posX += deltaX
                if (posY, posX, dir) in visited:
                    return True
                visited.add((posY, posX, dir))

    loopPositions = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == ".":
                grid[i] = grid[i][:j] + "#" + grid[i][j + 1:]
                if isLoop():
                    loopPositions += 1
                grid[i] = grid[i][:j] + "." + grid[i][j + 1:]
    
    print(loopPositions)

part2()
    
print(f"{time.time() - start_time:.4f}")


    