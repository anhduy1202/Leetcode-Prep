def countComponents(n, edges) -> int:
    #Build graph
    graph = {i:[] for i in range(n)}
    for edge in edges:
        child, parent = edge
        graph[child].append(parent)
        graph[parent].append(child)
    
    count = 0
    visited = set()
    
    # dfs
    def dfs(vertex):
        if vertex in visited:
            return
        visited.add(vertex)
        for v in graph[vertex]:
            dfs(v)

    # loop every vertices
    for nodes in range(n):
        if nodes not in visited:
            dfs(nodes)
            count += 1
    
    return count