class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.diameter = 0

    def findDiameter(self):
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            height = left + right
            self.diameter = max(self.diameter, height)
            return max(left, right)+1
        dfs(self)
        return self.diameter


Node4 = TreeNode(val=4)
Node5 = TreeNode(val=5)
Node2 = TreeNode(val=2, left=Node4, right=Node5)
Node3 = TreeNode(val=3)
root = TreeNode(val=1,left=Node2, right=Node3)
print(root.findDiameter())
