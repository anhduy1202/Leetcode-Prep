from TreeNode import TreeNode

# Left -> Right -> Root

def postOrderRecursive(root):
    res = []
    def postOrder(root):
        if not root:
            return
        postOrder(root.left)
        postOrder(root.right)
        res.append(root.val)
    postOrder(root)
    return res

def postOrderIterative(root):
    res = []
    if not root:
        return []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]

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

print(postOrderIterative(root))