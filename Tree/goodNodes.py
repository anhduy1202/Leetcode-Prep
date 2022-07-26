class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def goodNodes(self):
        self.res = 0
        self.maxInterval = float('inf')
        if not root:
            return 0

        def dfs(root,min):
            if not root:
                return
            if min <= root.val < self.maxInterval:
                self.res += 1
                min = root.val
            dfs(root.left,min)
            dfs(root.right,min)
        
        dfs(self,self.val)
        return self.res

Node3 = TreeNode(val=3)
Node5 = TreeNode(val=5)
Node1 = TreeNode(val=1)
Node1_1 = TreeNode(val=1,left=Node3)
Node4 = TreeNode(val=4,left=Node1,right=Node5)
root = TreeNode(val=3, left=Node1_1, right=Node4)
print(root.goodNodes())