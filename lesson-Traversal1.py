class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Return type: List[int]
def preOrderTraversal(node):
    #Base case
    if node is None:
        return []
    
    
    leftValues = preOrderTraversal(node.left)
    rightValues = preOrderTraversal(node.right)

    return [node.value] + leftValues + rightValues

#IN order print hiih
def inOrderTraversal(node):
    #Base case
    if node is None:
        return []
    
    
    leftValues = inOrderTraversal(node.left)
   # print(node.value, end=',')
    rightValues = inOrderTraversal(node.right) 
    return leftValues + [node.value] + rightValues 

#Post order print hiih
def postOrderTraversal(node):
    #Base case
    if node is None:
        return []
    
    
    leftValues =  inOrderTraversal(node.left)
    rightValues =  inOrderTraversal(node.right) 
   # print(node.value, end=',')

    return leftValues + rightValues + [node.value]
   


root = TreeNode(7)
root.left = TreeNode(5)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(2)
root.left.right = TreeNode(8)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(4)
print(preOrderTraversal(root))
print(inOrderTraversal(root))
# print()
# inOrderTraversal(root)
# print()
# postOrderTraversal(root)