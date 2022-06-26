class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def isSymm(left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return (isSymm(left.left,right.right) and isSymm(left.right,right.left))
        
    return isSymm(root.left,root.right)

node3L = TreeNode(val=3)
node4L = TreeNode(val=4)
node2L= TreeNode(val=2,left=node3L,right=node4L)
node3R = TreeNode(val=3)
node4R = TreeNode(val=4)
node2R = TreeNode(val=2,left=node4R,right=node3R)
root = TreeNode(val=1,left=node2L,right=node2R)
print(isSymmetric(root))