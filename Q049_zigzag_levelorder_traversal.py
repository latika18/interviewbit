Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example : 
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        st_crt_lvl =[A]
        st_nxt_lvl =[]
        ans_list = []
        
        while st_crt_lvl:
            u = st_crt_lvl[-1]
            ans_list.append(u) 
            if u.left:
                st_nxt_lvl.append(u.left)
            if u.right:
                st_nxt_lvl.append(u.right)
            while st_nxt_lvl:
                u = st_nxt_lvl.pop()
                ans_list.append(u)
                
                if u.right:
                    st_crt_lvl.append(u.right)
                if u.left:
                    st_crt_lvl.append(u.left)
                    
                    
        return ans_list
        
