
##Question 26
##Perform Depth first traversal on a BST and print the elements traversed
##Example Input:
##100,12,98,223,-78,-12,82,96,74,30,789,912,120

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
     

    def postorder(self,root):
##      left ,right , root

        if root:
            if root.left:
                self.postorder(root.left)
            if root.right:
                self.postorder(root.right)
            print root.value


    def inorder(self,root):
##        leftt,root,right
  
        if root.left:
            self.inorder(root.left)
        print root.value
        if root.right:
            self.inorder(root.right)
                        


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
print "postorder traversal is this "
t.postorder(t.root)
print "inorder traversal is this "
t.inorder(t.root)
