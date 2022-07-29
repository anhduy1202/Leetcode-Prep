from collections import deque
def maxAreaDFS(grid):
    maxArea = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(grid, r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 0
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        area = 1
        area += dfs(grid, r, c+1)
        area += dfs(grid, r, c-1)
        area += dfs(grid, r+1, c)
        area += dfs(grid, r-1, c)

        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                maxArea = max(dfs(grid, r, c), maxArea)

    return maxArea


def maxAreaBFS(grid):
    maxArea = 0
    rows = len(grid)
    cols = len(grid[0])

    def bfs(grid, r, c):
        q = deque([(r, c)])
        area = 0
        while q:
            row, col = q.popleft()
            if row < 0 or col < 0 or row >= rows or col >= cols:
                continue
            if grid[row][col] == 0:
                continue
            grid[row][col] = 0
            area += 1
            q.extend([(row+1, col)])
            q.extend([(row-1, col)])
            q.extend([(row, col+1)])
            q.extend([(row, col-1)])
        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                maxArea = max(bfs(grid, r, c), maxArea)

    return maxArea


print(maxAreaBFS([[1, 1, 1, 0, 0],
               [0, 1, 0, 0, 1],
               [0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0],
               [0, 0, 1, 0, 0]]))
