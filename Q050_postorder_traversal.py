Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3
return [3,2,1].


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        list = []
        stack = []
        stack.append(A)
        while stack:
            u = stack[-1]  ## assign the last element of stack
            if u.left == None and u.right == None: 
                list.append(u.val)
                stack = stack[:-1]
            if u.right:
                stack.append(u.right)
                u.right = None
            if u.left:
                stack.append(u.left)
                u.left = None
            
        
        return list    
               
