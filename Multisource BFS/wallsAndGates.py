from collections import deque

def wallsAndGates(room):
    rows = len(room)
    cols = len(room[0])
    q = deque()
    visited = [[False for j in range(cols)] for i in range(rows)]
    dist = 0
    for row in range(rows):
        for col in range(cols):
            if room[row][col] == 0:
                q.append((row, col))
                visited[row][col] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            room[r][c] = dist
            for ro, co in directions:
                dr = r + ro
                dc = c + co
                if dr < 0 or dc < 0 or dr >= rows or dc >= cols:
                    continue
                if visited[dr][dc] or room[dr][dc] == -1:
                    continue

                visited[dr][dc] = True
                q.append((dr, dc))
        dist += 1


print(wallsAndGates([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647,
      2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]))
