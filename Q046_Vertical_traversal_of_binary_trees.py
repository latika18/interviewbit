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
        
   def verticalordertraversal(self,root):
        visited = []
        hashmap = {}  ## hashmap to map hd to elements
        hd = 0  ## horizontal distance
        level = 0
        if root:
            visited.append(root)
            hashmap[hd] = root
        current = root
        while current:
            if current.left:
                
                hashmap[hd-1]  = current.left.value
                visited.append(current.left)
            if current.right:
                hashmap[hd+1] = current.right.value
                visited.append(current.right)
                
            visited.pop(0)
            if not visited:
                break
            hd = hd+1
            current = visited[0]
        return hashmap
