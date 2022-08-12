from TreeNode import TreeNode

def pathSum(root, targetSum):
    res = []

    def dfs(root, currSum, arr):
        if not root:
            return
        arr.append(root.val)
        if not root.left and not root.right and root.val == currSum:
            res.append(list(arr))
        else:
            dfs(root.left, currSum - root.val, arr)
            dfs(root.right, currSum - root.val, arr)
        arr.pop()

    dfs(root, targetSum, [])
    return res

Node4 = TreeNode(val=4)
Node5 = TreeNode(val=5)
Node2 = TreeNode(val=2)
Node7 = TreeNode(val=7)
Node7_1 = TreeNode(val=7,left=Node4,right=Node5)
Node9 = TreeNode(val=9,left=Node2,right=Node7)
root = TreeNode(val=1, left=Node7_1, right=Node9)
print(pathSum(root,12))