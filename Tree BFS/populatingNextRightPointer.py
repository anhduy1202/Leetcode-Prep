from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None,next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return []
    q = deque([root])
    while q:
        prevNode = None
        for _ in range(len(q)):
            node = q.popleft()
            if prevNode:
                prevNode.next = node
            prevNode = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return root

def connectCircular(root):
    if not root:
        return []
    q = deque([root])
    prevNode = None
    while q:
        node = q.popleft()
        if prevNode:
            prevNode.next = node
        prevNode = node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return root


Node4 = TreeNode(val=4)
Node5 = TreeNode(val=5)
Node6 = TreeNode(val=6)
Node7 = TreeNode(val=7)
Node2 = TreeNode(val=2,left=Node4,right=Node5)
Node3 = TreeNode(val=3,left=Node6,right=Node7)
root = TreeNode(val=1, left=Node2, right=Node3)
print(connectCircular(root))