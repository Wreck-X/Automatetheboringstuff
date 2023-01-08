import random, time, copy
HEIGHT = 60
WIDTH = 60

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)

while True:
    print('\n\n\n\n\n')
    currentcells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentcells[x][y],end = '')
        print()
    
    for x in range(WIDTH):
        for y in range(HEIGHT):

            # %1 ensures leftCoord is always between 0  and width - 1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1)  % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            numNeighbours = 0
            if currentcells[leftCoord][aboveCoord] == '#':
                numNeighbours +=  1
            if currentcells[x][aboveCoord] == '#':
                numNeighbours += 1
            if currentcells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1
            if currentcells[rightCoord][y] == '#':
                numNeighbours += 1
            if currentcells[leftCoord][belowCoord] == '#':
                numNeighbours += 1
            if currentcells[x][belowCoord] == '#':
                numNeighbours += 1
            if currentcells[rightCoord][belowCoord] == '#':
                numNeighbours += 1
            if currentcells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = '#'
            elif currentcells[x][y] == ' ' and numNeighbours == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
    time.sleep(1)