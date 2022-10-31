from TreeNode import TreeNode

def merge(root1, root2):
    if not root1 and not root2:
        return None
    if root1 and not root2:
        return root1
    if not root1 and root2:
        return root2
    root = TreeNode(root1.val + root2.val)
    root.left = merge(root1.left, root2.left)
    root.right = merge(root1.right, root2.right)
    return root