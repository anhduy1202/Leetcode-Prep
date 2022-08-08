from TreeNode import TreeNode
from collections import deque
def zigzagOrder(root):
    if not root:
        return []
    q = deque([root])
    res = []
    changeOrder = True
    while q:
        currentLevel = deque()
        for _ in range(len(q)):
            node = q.popleft()
            if changeOrder:
                currentLevel.append(node.val)
            else:
                currentLevel.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        changeOrder = not changeOrder
        res.append(list(currentLevel))
    return res


Node4 = TreeNode(val=4)
Node5 = TreeNode(val=5)
Node6 = TreeNode(val=6)
Node7 = TreeNode(val=7)
Node2 = TreeNode(val=2,left=Node4,right=Node5)
Node3 = TreeNode(val=3,left=Node6,right=Node7)
root = TreeNode(val=1,left=Node2,right=Node3)
print(zigzagOrder(root))