from collections import deque
def shortestBridge(grid):
    # 1. DFS to find the first island
    # 2. BFS to find the shortest bridge to the other island
    visited = set()
    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(row,col):
        if row < 0 or col < 0 or row >= ROWS or col >= COLS:
            return
        if (row,col) in visited:
            return
        if grid[row][col] == 0:
            return
        visited.add((row,col))
        dfs(row+1,col)
        dfs(row-1,col)
        dfs(row,col+1)
        dfs(row,col-1)

    def bfs():
        # Convert set to a queue
        q = deque()
        for number in visited:
            r,c = number
            q.append((r,c,0))
        # BFS to find the shortest
        while q:
            row,col,distance = q.popleft()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for r,c in directions:
                dr = r + row
                dc = c + col
                if dr < 0 or dc < 0 or dr >= ROWS or dc >= COLS:
                    continue
                if (dr,dc) in visited:
                    continue
                if grid[dr][dc]: # Reach the other island
                    return distance
                visited.add((dr,dc))
                q.append((dr,dc,distance+1))

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                dfs(row,col)
                # call bfs() right when we've found 1 island ( only 2 islands total )
                return bfs()