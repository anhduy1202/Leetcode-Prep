from TreeNode import TreeNode
from collections import deque
def reversedLeverOrder(root):
    if not root:
        return []
    q = deque([root])
    res = deque()
    while q:
        currentLevel = []
        for _ in range(len(q)):
            node = q.popleft()
            currentLevel.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.appendleft(currentLevel)
    return res


Node4 = TreeNode(val=4)
Node5 = TreeNode(val=5)
Node6 = TreeNode(val=6)
Node7 = TreeNode(val=7)
Node2 = TreeNode(val=2,left=Node4,right=Node5)
Node3 = TreeNode(val=3,left=Node6,right=Node7)
root = TreeNode(val=1,left=Node2,right=Node3)
print(reversedLeverOrder(root))