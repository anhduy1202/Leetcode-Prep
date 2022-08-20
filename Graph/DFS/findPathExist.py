def validPath(n, edges, source, destination):

    if len(edges) == 0:
        return True

    # Initilize graph
    graph = {i: [] for i in range(n)}
    visited = set()

    # Build graph
    for edge in edges:
        parent, child = edge
        graph[parent].append(child)
        graph[child].append(parent)

    stack = [source]
    visited.add(source)
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor == destination:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return False


print(validPath(6,[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],0,5))
