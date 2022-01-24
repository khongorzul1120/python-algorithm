class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Pre order print hiih
def preOrderTraversal(node):
    #Base case
    if node is None:
        return
    
    print(node.value, end=',')
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

#IN order print hiih
def inOrderTraversal(node):
    #Base case
    if node is None:
        return
    
    
    inOrderTraversal(node.left)
    print(node.value, end=',')
    inOrderTraversal(node.right)  

#Post order print hiih
def postOrderTraversal(node):
    #Base case
    if node is None:
        return
    
    
    inOrderTraversal(node.left)
    inOrderTraversal(node.right) 
    print(node.value, end=',')


root = TreeNode(7)
root.left = TreeNode(5)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(2)
root.left.right = TreeNode(8)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(4)
preOrderTraversal(root)
print()
inOrderTraversal(root)
print()
postOrderTraversal(root)