from collections import deque
def numIslandsDFS(grid):
    islands = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(grid, r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols):
            return
        if grid[r][c] == "0":
            return

        grid[r][c] = "0"
        dfs(grid, r+1, c)
        dfs(grid, r-1, c)
        dfs(grid, r, c+1)
        dfs(grid, r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(grid, r, c)
    return islands

def numIslandsBFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    totalIslands = 0

    for i in range(rows):
        for j in range(cols):
            if (matrix[i][j] == "1"):  # only if the cell is a land
                # we have found an island
                totalIslands += 1
                visitIslandBFS(matrix, i, j)
    return totalIslands


def visitIslandBFS(matrix,  x,  y):
    neighbors = deque([(x, y)])
    while neighbors:
        row, col = neighbors.popleft()

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue  # continue, if it is not a valid cell
        if matrix[row][col] == "0":
            continue  # continue if it is a water cell

        matrix[row][col] = "0"  # mark the cell visited by making it a water cell

        # insert all neighboring cells to the queue for BFS
        neighbors.extend([(row + 1, col)])  # lower cell
        neighbors.extend([(row - 1, col)])  # upper cell
        neighbors.extend([(row, col + 1)])  # right cell
        neighbors.extend([(row, col - 1)])  # left cell

# print(numIslandsDFS([
#     ["1","1","1","0","0"],
#     ["0","1","0","0","1"],
#     ["0","0","1","1","0"],
#     ["0","0","1","0","0"],
#     ["0","0","1","0","0"],
#     ]))

print(numIslandsBFS([
    ["1","1","1","0","0"],
    ["0","1","0","0","1"],
    ["0","0","1","1","0"],
    ["0","0","1","0","0"],
    ["0","0","1","0","0"],
    ]))