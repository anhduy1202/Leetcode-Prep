from faulthandler import disable


def distinctIslands(grid):
    rows = len(grid)
    columns = len(grid[0])
    visited = [[False for i in range(columns)] for j in range(rows)]
    islandSet = set()

    def traverseIslandsDFS(r, c, direction):
        if r < 0 or c < 0 or r >= rows or c >= columns:
            return ""
        if grid[r][c] == 0 or visited[r][c]:
            return ""
        visited[r][c] = True
        islandTraversal = direction
        islandTraversal += traverseIslandsDFS(r+1, c, "D")
        islandTraversal += traverseIslandsDFS(r-1, c, "U")
        islandTraversal += traverseIslandsDFS(r, c+1, "R")
        islandTraversal += traverseIslandsDFS(r, c-1, "L")
        islandTraversal += "B"
        return islandTraversal
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1 and not visited[r][c]:
                path = traverseIslandsDFS(r, c, "O")
                islandSet.add(path)
    
    return len(islandSet)

print(distinctIslands(
[[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]]))
