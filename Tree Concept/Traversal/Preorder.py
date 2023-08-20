from TreeNode import TreeNode

# Root -> Left -> Right

def preOrderRecursive(root):
    res = []
    def preOrder(root):
        if not root:
            return
        res.append(root.val)
        preOrder(root.left)
        preOrder(root.right)
    preOrder(root)
    return res

def preOrderIterative(root):
    res = []
    if not root:
        return []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

NodeC = TreeNode(val="C")
NodeE = TreeNode(val="E")
NodeH = TreeNode(val="H")
NodeI = TreeNode(val="I",left=NodeH)
NodeG = TreeNode(val="G",right=NodeI)
NodeA = TreeNode(val="A")
NodeD = TreeNode(val="D",left=NodeC,right=NodeE)
NodeB = TreeNode(val="B",left=NodeA,right=NodeD)
root = TreeNode(val="F",left=NodeB,right=NodeG)

#               F
#       B               G      
#   A       D               I
#         C   E           H

print(preOrderIterative(root))