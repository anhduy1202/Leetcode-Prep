def closedIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for i in range(cols)] for j in range(rows)]
    islands = 0

    def closedIslandsDFS(grid, r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False  # Out of bounds
        if grid[r][c] == 1 or visited[r][c]:
            return True  # surrounded by 1

        visited[r][c] = True
        isClosed = True
        isClosed &= closedIslandsDFS(grid, r+1, c)
        isClosed &= closedIslandsDFS(grid, r-1, c)
        isClosed &= closedIslandsDFS(grid, r, c+1)
        isClosed &= closedIslandsDFS(grid, r, c-1)
        return isClosed

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and not visited[r][c]:
                if closedIslandsDFS(grid, r, c):
                    islands += 1

    return islands


print(closedIslands([[1, 1, 1, 1, 1, 1, 1, 0], 
                     [1, 0, 0, 0, 0, 1, 1, 0], 
                     [1, 0, 1, 0, 1, 1, 1, 0], 
                     [1, 0, 0, 0, 0, 1, 0, 1], 
                     [1, 1, 1, 1, 1, 1, 1, 0]]))
