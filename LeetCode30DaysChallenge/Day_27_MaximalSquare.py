def maximalSquare(matrix):
    rows = len(matrix)

    if rows == 0:
        return 0
    
    cols = len(matrix[0])
    
    # matrix = int(map(int, matrix))
    # matrix = [[int(k) for k in matrix[l]] for l in matrix]
    matrix2 = []
    for x in matrix:
        matrix2.append(list(map(int, x)))

    matrix = matrix2

    S = [[0 for k in range(cols+1)] for l in range(rows+1)]
    
    for i in range(0, rows): 
        for j in range(0, cols): 
            if (matrix2[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j], 
                            S[i-1][j-1]) + 1
            else: 
                S[i][j] = 0
    
    max_of_s = max(map(max, S))
    
    return max_of_s**2
    
matrix = [[]]

print(maximalSquare(matrix))