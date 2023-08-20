def solve(board):
    ROWS = len(board)
    COLS = len(board[0])

    def borderRegions(r,c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
            return
        board[r][c] = "T"
        borderRegions(r+1,c)
        borderRegions(r-1,c)
        borderRegions(r,c+1)
        borderRegions(r,c-1)
    
    # Check for border region
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "O" and (row in [0, ROWS - 1] or col in [0, COLS - 1]):
                borderRegions(row,col)

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "O":
                board[row][col] = "X"
    
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "T":
                board[row][col] = "O"
    
    return board

print(solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))