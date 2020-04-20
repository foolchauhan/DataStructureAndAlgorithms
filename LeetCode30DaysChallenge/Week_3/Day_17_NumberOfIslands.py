def numIslands(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    
    noOfIslands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                markCurrentIsland(grid, i, j, rows, cols)
                noOfIslands += 1
    
    return noOfIslands

def markCurrentIsland(grid, i, j, rows, cols):
    if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!='1':
        return
    
    grid[i][j] = 2

    markCurrentIsland(grid, i+1, j, rows, cols)
    markCurrentIsland(grid, i, j+1, rows, cols)
    markCurrentIsland(grid, i-1, j, rows, cols)
    markCurrentIsland(grid, i, j-1, rows, cols)

grid = [["1","0","1","1","0","1","1"]]

print(numIslands(grid))
