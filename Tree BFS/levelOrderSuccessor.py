from TreeNode import TreeNode
from collections import deque


def levelOrderSuccessor(root, givenNode):
    if not root:
        return None
    q = deque([root])
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        if node.val == givenNode:
            break
    return q[0].val if q else None

Node9 = TreeNode(val=9)
Node10 = TreeNode(val=10)
Node5 = TreeNode(val=5)
Node7 = TreeNode(val=7, left=Node9)
Node1 = TreeNode(val=1, left=Node10, right=Node5)
root = TreeNode(val=12, left=Node7, right=Node1)
print(levelOrderSuccessor(root, 12))
