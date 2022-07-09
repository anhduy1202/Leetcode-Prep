from copy import deepcopy
def gameOfLife(board):
    rows = len(board)
    columns = len(board[0])
    temp = deepcopy(board)

    def bfs(r,c):
        row,col = r,c
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        live = 0
        for ro,co in directions:
            dr = ro + row
            dc = co + col
            if dr >= 0 and dc >= 0 and dr < rows and dc < columns:
                if board[dr][dc] == 1: #live neighbor
                    live += 1
        if board[row][col] == 1:
            if live < 2 or live > 3: temp[row][col] = 0
            else: temp[row][col] = 1
        else:
            if live == 3: temp[row][col] = 1
   
    for r in range(len(board)):
        for c in range(len(board[0])):
            bfs(r,c)
    return temp

print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))