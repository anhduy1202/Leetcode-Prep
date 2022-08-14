from collections import deque


def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    visited = set()
    
    def dfs(row,col,length):
        if length == len(word):
                return True
        if row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visited:
            return False
        if board[row][col] != word[length]:
            return False
        visited.add((row,col))
        res = (dfs(row+1,col,length+1) or 
                dfs(row-1,col,length+1) or 
                dfs(row,col+1,length+1) or 
                dfs(row,col-1,length+1))
        visited.remove((row,col))
        return res
    for row in range(rows):
        for col in range(cols):
            if dfs(row,col,0): 
                return True
    
    return False


print(exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
            ,"ABCESEEEFS"))
