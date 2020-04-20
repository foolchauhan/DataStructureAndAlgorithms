def minPathSum(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    tc = [[0 for x in range(cols)] for x in range(rows)] 
    tc[0][0] = grid[0][0]

    for i in range(1, rows): 
        tc[i][0] = tc[i-1][0] + grid[i][0] 
    
    for j in range(1, cols): 
        tc[0][j] = tc[0][j-1] + grid[0][j] 
    
    for i in range(1, rows): 
        for j in range(1, cols): 
            tc[i][j] = min(tc[i-1][j], tc[i][j-1]) + grid[i][j] 
  
    return tc[rows-1][cols-1] 
