Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].
##Code

class Node(object):
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, value):
        self.root = Node(value)
        

    def insert(self, value):
        current = self.root
        while current:
            if value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left

            
    def Breadth_first_search(self,root):
        """In BFS the Node Values at each level of the Tree are traversed before going to next level"""

        visited = []
        if root:
            visited.append(root)
            print root.value
        current = root
        while current :
            if current.left:
                print current.left.value
                visited.append(current.left)
            if current.right:
                print current.right.value
                visited.append(current.right)
            visited.pop(0)
            
            if not visited:
                break
            
            
            current = visited[0]
            
        
               
  
t = BinarySearchTree(100)
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

print "Output of Breadth First search is "
t.Breadth_first_search(t.root)







                    
    

