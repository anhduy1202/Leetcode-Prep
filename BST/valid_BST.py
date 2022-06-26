
class BSTreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):

    def valid(node, left, right):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False

        return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
    return valid(root,float("-inf"),float("inf"))

node2 = BSTreeNode(val=2)
node3 = BSTreeNode(val=3)
node4 = BSTreeNode(val=4)
node7 = BSTreeNode(val=7)
node6 = BSTreeNode(val=6, left=node3, right=node7)
root = BSTreeNode(val=5, left=node4, right=node6)

print(isValidBST(root))
