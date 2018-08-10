Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3
return [3,2,1].

Using recursion is not allowed.

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST(object):
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        current = self.root
        while current:
            if value > current.value:
                if current.right is None:
                    current.right  = Node(value)
                    break
                else:
                    current = current.right
            else:
                if current.left is None :
                    current.left  = Node(value)
                    break
                else:
                    current = current.left

   
     

    def postorder(self,root):
##      left ,right , root

        if root:
            if root.left:
                self.postorder(root.left)
            if root.right:
                self.postorder(root.right)
            print root.value


t = BST(100)
t.insert(12)
t.insert(92)
t.insert(112)
t.insert(123)
t.insert(2)
t.insert(11)
t.insert(52)
t.insert(3)
t.insert(66)
t.insert(10)
print t.root

print "postorder traversal is this "
t.postorder(t.root)
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
        l = []
        st = []
        st.append(A)
        while st:
            u = st[-1]
            if u.left == None and u.right == None: 
                l.append(u.val)
                st = st[:-1]
            if u.right:
                st.append(u.right)
                u.right = None
            if u.left:
                st.append(u.left)
                u.left = None
            
        
        return l    
               
