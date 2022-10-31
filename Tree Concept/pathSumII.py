from TreeNode import TreeNode

def pathSumRecursive(root, targetSum):
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

def pathSumIterative(root, targetSum):
    if not root:
        return []
    stack = [(root,targetSum,[root.val])]
    res = []
    while stack:
        node, currSum, path = stack.pop()
        if not node.left and not node.right:
            if currSum == node.val:
                res.append(path)
        if node.left:
            stack.append((node.left, currSum - node.val, path+[node.left.val]))
        if node.right:
            stack.append((node.right, currSum - node.val, path+[node.right.val]))
    return res

Node4 = TreeNode(val=4)
Node5 = TreeNode(val=5)
Node2 = TreeNode(val=2)
Node7 = TreeNode(val=7)
Node7_1 = TreeNode(val=7,left=Node4,right=Node5)
Node9 = TreeNode(val=9,left=Node2,right=Node7)
root = TreeNode(val=1, left=Node7_1, right=Node9)
print(pathSumRecursive(root,12))