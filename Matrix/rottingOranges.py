from collections import deque


def orangesRotting(grid):
    q = deque()
    fresh, minute = 0,0
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                q.append((row,col))
            if grid[row][col] == 1:
                fresh += 1
    directions = [(0,1),(0,-1),(1,0),(-1,0)]     
    while q and fresh > 0:
        for _ in range(len(q)):
            ro,co = q.popleft()
            for r,c in directions:
                dr = ro + r
                dc = co + c
                if dr < 0 or dr >= rows or dc < 0 or dc >= cols: 
                    continue
                if grid[dr][dc] != 1:
                    continue
                grid[dr][dc] = 2
                q.append((dr,dc))
                fresh -= 1
        minute += 1
    return minute if fresh == 0 else -1

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))