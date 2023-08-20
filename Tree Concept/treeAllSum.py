'''
Given a Binary Tree, return all sum from node to leaves
Ex:
        5
    2       1
 3     4        6

return [21,9,3,4,7,6]   
'''

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def findAllSum(root):
    if not root:
        return []
    res = []
    def dfsSum(root):
        if not root: 
            return 0
        else:
            currSum = root.val
            currSum += dfsSum(root.left)
            currSum += dfsSum(root.right)
            res.append(currSum)
        return currSum
    dfsSum(root)
    return res

NODE3 = TreeNode(val=3)
NODE4 = TreeNode(val=4)
NODE6 = TreeNode(val=6)
NODE1 = TreeNode(val=1, right=NODE6)
NODE2 = TreeNode(val=2, left=NODE3, right=NODE4)
root = TreeNode(val=5, left=NODE2, right=NODE1)
print(findAllSum(root))