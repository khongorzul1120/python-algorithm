class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    
#    7
#   /  \
#  6    5
# / \
#1   2


node1 = TreeNode(7)
node2 = TreeNode(3)
node3 = TreeNode(2)

node1.left = node2
node1.right = node3

node2.left = TreeNode(1)
node2.right = TreeNode(2)


# Recursion ---- Fibanocci sequence 
# 
# [1,1,2,3,5,8,13,21,34,55 ....] - Fibanocci sequence daraagiin too ni umnuh 2 toonii  niilber baina 

def fib(n):
    #Base case
    if n <= 2:
        return 1
    
    return fib(n-1) + fib(n-2)