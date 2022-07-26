class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.diameter = 0

    def rightSideView(self):
        self.ans = []

        def dfs(root, depth):
            if root == None:
                return
            # When we meet this `depth` for the first time, let's add the first node as the right side most node.
            if depth == len(self.ans):
                self.ans.append(root.val)
            dfs(root.right, depth + 1)  # Go right side first
            dfs(root.left, depth + 1)

        dfs(self, 0)
        return self.ans

Node3 = TreeNode(val=3)
Node5 = TreeNode(val=5)
Node4 = TreeNode(val=4, left=Node3, right=Node5)
Node0 = TreeNode(val=0)
Node2 = TreeNode(val=2, left=Node0, right=Node4)
Node2_1 = TreeNode(val=2)
Node9 = TreeNode(val=9)
Node8 = TreeNode(val=8, left=Node2_1, right=Node9)
root = TreeNode(val=6, left=Node2, right=Node8)
print(root.rightSideView())
