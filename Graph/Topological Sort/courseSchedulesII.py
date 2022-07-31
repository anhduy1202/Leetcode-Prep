from collections import deque

def courseScheduleII(numCourses, prerequisites):
    res = []
    if len(prerequisites) == 0:
        return [ i for i in range(numCourses)]
    
    # Initialize the graph
    in_degrees = {i:0 for i in range(numCourses)}
    graph = {i:[] for i in range(numCourses)}
    
    # Build graph
    for edge in prerequisites:
        parent,child = edge
        graph[parent].append(child)
        in_degrees[child] += 1
    
    # Find sources
    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)
    
    # Getting topo order
    while sources:
        vertex = sources.popleft()
        res.append(vertex)
        for child in graph[vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)
    
    # Impossible to schedule
    if len(res) != numCourses:
        return []
    
    return res[::-1]

print(courseScheduleII(4,[[1,0],[2,0],[3,1],[3,2]]))