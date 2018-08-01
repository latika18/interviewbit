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

    def preorder(self,root):
##        root,left,right
        
      if root:
          print root.value
          if root.left:
                self.preorder(root.left)
          if root.right:
                self.preorder(root.right)
     

    
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
print "preorder traversal is this "
t.preorder(t.root)
