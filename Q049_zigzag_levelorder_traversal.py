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

def zigzagLevelOrder(A):

    st_crt_lvl = [A] # initialize
    ans_list = []   

    level = 0
    while st_crt_lvl: # check if all levels are processed
        st_nxt_lvl =[] # temporary queue to hold the next level elements
        tmp = [] # temporary storage to append to the ans_list 
        while st_crt_lvl:
            u = st_crt_lvl.pop(0)
            tmp.append(u.val) 
            if u.left:
                st_nxt_lvl.append(u.left)
            if u.right:
                st_nxt_lvl.append(u.right)                
        if (len(tmp) > 0): # if tmp is not empty
            if level % 2 == 1: # ensure zig-zag level order traversal
                tmp = tmp[::-1]
            ans_list.append(tmp)
        st_crt_lvl = st_nxt_lvl  # copy the temporary queue to the current queue      
        level += 1

    return ans_list


class BinaryTree:
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.val = data

A = BinaryTree(None, None, 3)
A.left = BinaryTree(None, None, 9)
A.right = BinaryTree(None, None, 20)
A.left.left = BinaryTree(None, None, 1)
A.left.right = BinaryTree(None, None, 2)
A.right.left = BinaryTree(None, None, 15)
A.right.right = BinaryTree(None, None, 7)
zigzagLevelOrder(A)
# [[3], [20, 9], [1, 2, 15, 7]]
        
