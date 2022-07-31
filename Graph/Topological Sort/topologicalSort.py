from collections import deque
def topoLogicalSort(vertices,edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # 1. Initialize the graph
    in_degrees = {i:0 for i in range(vertices)}
    graph = {i:[] for i in range(vertices)}

    # 2. Build the graph
    for edge in edges:
        parent,child = edge
        graph[parent].append(child)
        in_degrees[child] += 1
    
    # 3. Find all sources (vertices with 0 in-degree)
    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)
    
    # 4. For each source, add it to the sortedOrder and subtract '1' from all of its 
  # children's in-degrees if a child's in-degree becomes zero, add it to sources queue
    
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:  # get the node's children to decrement their in-degrees
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)
    
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder

print(topoLogicalSort(7,[[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))