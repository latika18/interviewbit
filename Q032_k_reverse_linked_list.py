Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

 NOTE : The length of the list is divisible by K 
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

Try to solve the problem using constant extra space.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self,seq):
        """prepends item of lists into linked list"""
        self.head = None
        for item in seq:
            node = ListNode(item)
            node.next = self.head
            self.head = node

    def reverseList(self, B):
        A = self.head
        
        current = A
        C = B 
        if B == 1:
            return A
        
        cnt = 0
        while current:
            current = current.next
            cnt += 1
        print cnt
        while cnt != 0:
            cnt = cnt -C
            B = C
            prev = None
            print "cnt", cnt
            while B != 0 and A:
                temp = A.next
                A.next = prev
                prev = A
                A = temp
                B -= 1
            print "A", A.val

    
            
        return prev.val
        
              
    
       
##llist = Solution([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7])
##print llist.reverseList(1)
llist_1 = Solution([ 1,2,3,4,5,6])
print llist_1.reverseList(3)

                 
##listpal_2 = Solution([6 , 3 , 7, 3, 6])
##assert listpal_2.list_palin()
##listpal_3 = Solution([3, 7 ,3 ])
##assert listpal_3.list_palin()
##listpal_4 = Solution([1])
##assert listpal_4.list_palin()

