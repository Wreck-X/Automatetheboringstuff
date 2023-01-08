import copy

grid = [['.', '.', '.', '.', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['O', 'O', 'O', 'O', '.', '.'],['O', 'O', 'O', 'O', 'O', '.'],['.', 'O', 'O', 'O', 'O', 'O'],['O', 'O', 'O', 'O', 'O', '.'],['O', 'O', 'O', 'O', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['.', '.', '.', '.', '.', '.']]
height = len(grid)
width = len(grid[0])

for i in range(width):
    for j in range(height):
        print(grid[j][i],end = ' ')
    print()