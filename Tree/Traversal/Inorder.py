from TreeNode import TreeNode

# Left -> Root -> Right

def inOrderRecursive(root):
    res = []
    def inOrder(root):
        if not root:
            return
        inOrder(root.left)
        res.append(root.val)
        inOrder(root.right)
    inOrder(root)
    return res

def inOrderIterative(root):
    if not root:
        return []
    res = []
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
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

print(inOrderIterative(root))