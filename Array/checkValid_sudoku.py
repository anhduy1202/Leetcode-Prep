from collections import defaultdict


def checkValid(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rowSet = defaultdict(set)
    colSet = defaultdict(set)
    resSet = set(range(1,rows+1))

    for r in range(rows):
        for c in range(columns):
            rowSet[r].add(matrix[r][c])
            colSet[c].add(matrix[r][c])

    for key in rowSet:
        if rowSet[key] != resSet:
            return False

    for key in colSet:
        if colSet[key] != resSet:
            return False
    return True


print(checkValid([[1,2,3],[3,1,2],[2,3,1]]))
