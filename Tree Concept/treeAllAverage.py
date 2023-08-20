'''
Given a Binary Tree, return all average from node to leaves
Ex:
        5
    2       1
 3     4        6

return [3.5,3,3,4,3.5,6]   
'''

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def findAllAvg(root):
    if not root:
        return []
    res = []

    def height(root):
        if not root:
            return 0
        left = height(root.left)
        right = height(root.right)
        return max(left,right) + 1
    treeHeight = height(root)

    def dfsAvg(root, count):
        if not root: 
            return 0
        else:
            currSum = root.val
            currSum += dfsAvg(root.left, count + 1)
            currSum += dfsAvg(root.right, count + 1)
            if count > 0:
                res.append(currSum / (treeHeight - count))
        return currSum
    dfsAvg(root,0)
    return res

NODE3 = TreeNode(val=3)
NODE4 = TreeNode(val=4)
NODE6 = TreeNode(val=6)
NODE1 = TreeNode(val=1, right=NODE6)
NODE2 = TreeNode(val=2, left=NODE3, right=NODE4)
root = TreeNode(val=5, left=NODE2, right=NODE1)
print(findAllAvg(root))