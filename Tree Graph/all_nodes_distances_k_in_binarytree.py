from TreeNode import TreeNode
from collections import defaultdict,deque

def distanceK(root: TreeNode, target: TreeNode, k: int):
    # intialize graph
    graph = defaultdict(list)
    stack = [(root, None)]
    res = []

    # Build graph
    while stack:
        node, parent = stack.pop()
        if parent:
            graph[node.val].append(parent.val)
        if node.left:
            graph[node.val].append(node.left.val)
            stack.append((node.left, node))
        if node.right:
            graph[node.val].append(node.right.val)
            stack.append((node.right, node))

    visited = set()
    visited.add(target.val)
    # BFS target node

    def bfs(node, K):
        q = deque()
        q.append((node, K))
        while q:
            node, K = q.popleft()
            if K == 0:
                res.append(node)
            else:
                visited.add(node)
                for adj_node in graph[node]:
                    if adj_node not in visited:
                        q.append((adj_node, K-1))

    bfs(target.val, k)
    return res


Node8 = TreeNode(val=8)
Node7 = TreeNode(val=7)
Node6 = TreeNode(val=6, left=Node7, right=Node8)
Node5 = TreeNode(val=5)
Node3 = TreeNode(val=3, left=Node5, right=Node6)
Node4 = TreeNode(val=4)
root = TreeNode(val=2, left=Node3, right=Node4)
print(distanceK(root,Node8,3))
