Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
#final working solution on shell, also include code for reverse
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def __init__(self,seq):
         self.head = None
         for item in seq:
              node = ListNode(item)
              node.next = self.head
              self.head = node
              
    
    def reverse(self):
        current = self.head
        prev = None
        while (current is not None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        self.head = prev
        reverse_list = []
        while prev:
            reverse_list.append(prev.val)
            prev = prev.next
        return reverse_list
    
    def lPalin(self):
        node = self.head
        fast = node
        prev = None
        ispal = True
        
        while fast and fast.next:
            fast = fast.next.next
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        if fast:
            tail = node.next
        else:
            tail = node
      
       
        while prev and ispal:
                      
            if prev.val == tail.val:
                tail = tail.next
                prev = prev.next
                ispal = True
            else:
                 ispal = False
                 break
      
        if ispal :
            return 1
        else :
            return 0

listpal = Solution([7, 8, 6 ,  3 , 7 , 3 , 6, 8, 7 ])
print listpal.reverse()
print listpal.lPalin()
