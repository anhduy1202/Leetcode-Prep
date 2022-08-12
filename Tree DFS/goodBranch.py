from cgitb import reset
from TreeNode import TreeNode

count = 0
def goodBranch(root):
    dfs(root,root.val)
    return count

def dfs(root,minInterval):
    global count
    if not root:
        return 
    if (minInterval < root.val < float('inf')):
        minInterval = root.val
    if not root.left and not root.right:
        if minInterval <= root.val < float('inf'):
            count += 1

    dfs(root.left,minInterval)
    dfs(root.right,minInterval)
    
    
Node5 = TreeNode(val=5)
NodeM1 = TreeNode(val=-1)
Node6 = TreeNode(val=6)
Node7 = TreeNode(val=7)
Node2 = TreeNode(val=2,left=Node5,right=NodeM1)
Node4 = TreeNode(val=4,left=Node6,right=Node7)
root = TreeNode(val=1,left=Node2,right=Node4)
print(goodBranch(root))