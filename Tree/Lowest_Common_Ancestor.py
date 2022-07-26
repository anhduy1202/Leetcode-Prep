class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lca(root, p, q):
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        if p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root.val


Node3 = TreeNode(val=3)
Node5 = TreeNode(val=5)
Node4 = TreeNode(val=4, left=Node3, right=Node5)
Node0 = TreeNode(val=0)
Node2 = TreeNode(val=2, left=Node0, right=Node4)
Node2_1 = TreeNode(val=2)
Node9 = TreeNode(val=9)
Node8 = TreeNode(val=8, left=Node2_1, right=Node9)
root = TreeNode(val=6, left=Node2, right=Node8)
print(lca(root,Node0,Node5))
