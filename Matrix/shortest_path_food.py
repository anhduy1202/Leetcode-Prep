from collections import deque
def getFood(grid):
    rows = len(grid)
    cols = len(grid[0])
    step = 0
    visited = [[False for i in range(cols)] for j in range(rows)]
    def bfs(r, c,steps):
        q = deque()
        q.append((r,c,0))
        while q:
            r,c,steps = q.popleft()
            if r < 0 or c < 0 or r >= rows or c >= cols:
                continue
            if grid[r][c] == "X" or visited[r][c]:
                continue
            if grid[r][c] == "#":
                return steps
            visited[r][c] = True
            q.extend([(r+1,c,steps+1)])
            q.extend([(r-1,c,steps+1)])
            q.extend([(r,c+1,steps+1)])
            q.extend([(r,c-1,steps+1)])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "*":
                step = bfs(r,c,0)
    return -1 if step == None else step



print(getFood( [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]))