from collections import deque
def getFood(grid):
    rows = len(grid)
    cols = len(grid[0])
    step = 0
    visited = [[False for i in range(cols)] for j in range(rows)]
    def bfs(r, c,steps):
        q = deque()
        q.append((r,c,0))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r,c,steps = q.popleft()
            for ro,co in directions:
                dr = r + ro
                dc = c + co
                if dr < 0 or dc < 0 or dr >= rows or dc >= cols:
                    continue
                if grid[dr][dc] == "X" or visited[dr][dc]:
                    continue
                if grid[dr][dc] == "#":
                    return steps+1
                visited[dr][dc] = True
                q.append((dr,dc,steps+1))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "*":
                step = bfs(r,c,0)
    return -1 if step == None else step



print(getFood([["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]))