Given a binary tree, print a vertical order traversal of it.

Example :
Given binary tree:

      6
    /   \
   3     7
  / \     \
 2   5     9
returns

[
    [2],
    [3],
    [6 5],
    [7],
    [9]
]
Note : If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.
      
Code:      
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers 
    def __init__(self,root):
        self.root = TreeNode(value)
        
    def insert(self,value):
        current = A
        while current:
            if value > current.value:
                if current.right is None:
                    current.right = TreeNode(value)
                    break
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = TreeNode(value)
                    break
                else:
                    current = current.left
                    
        
    
    def verticalOrderTraversal(self, A):
        if A.left:
            self.verticalOrderTraversal(A.left)
        
        print root.value
        if root.right:
            self.verticalOrderTraversal(root.right)
