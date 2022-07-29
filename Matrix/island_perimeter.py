def isLandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    def dfs(grid, r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 1
        if grid[r][c] == 0:
            return 1
        if visited[r][c]:
            return 0
        visited[r][c] = True
        perimeter = 0
        perimeter += dfs(grid, r+1, c)
        perimeter += dfs(grid, r-1, c)
        perimeter += dfs(grid, r, c+1)
        perimeter += dfs(grid, r, c-1)
        return perimeter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return dfs(grid, r, c)


print(isLandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
