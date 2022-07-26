class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def validateBST(root):
    def dfs(root, left, right):
        if not root:
            return True
        if not (left < root.val and right > root.val):
            return False
        return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)

    return dfs(root, float('-inf'), float('inf'))


Node9 = TreeNode(val=9)
Node5 = TreeNode(val=5)
Node1 = TreeNode(val=1)
Node4 = TreeNode(val=4, left=Node9, right=Node5)
root = TreeNode(val=5, left=Node1, right=Node4)
print(validateBST(root))
