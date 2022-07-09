from collections import defaultdict


def validSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    square = defaultdict(set)
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == ".":
                continue
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3, c//3)]:
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            square[(r//3, c//3)].add(board[r][c])
    return True


print(validSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
