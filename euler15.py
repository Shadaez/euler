#Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking)
#to the bottom right corner.


#How many routes are there through a 20 x 20 grid?
grid = [[] for i in range(21)]
x = 1
z = 0
y = 1
rng = range(0,21)
for i in rng:
    grid[i].append(1)
    if i != 0:
        grid[0].append(1)

  
while y <= 20:
    while x  <= 20:
        if x == y and y != 0:
            grid[x].append(int(grid[x][y-1])*2)
        else:
             grid[x].append(int(grid[x][y-1]) + int(grid[x-1][y]))
        x += 1
    x = 1
    y += 1
    z += 1
for i in grid:
    print i
