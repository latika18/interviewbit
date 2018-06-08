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

    def reverseList(self, A, B):
        self.head = A
        prev = None
        current = A
        last_head=None
        if B == 1:
            return current
        cnt = 0
        while cnt < B and current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            cnt += 1

        if A:
            A.next = self.reverseList(current, B)
                     
        return prev

    def print_list(self):
        temp = self.head
        while(temp):
            print temp.val
            temp = temp.next
              
    
       
##llist = Solution([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7])
##print llist.reverseList(1)
llist_1 = Solution([ 1,2,3,4,5,6])
print llist_1.print_list()

llist_1.head = llist_1.reverseList(llist_1.head, 3)
print llist_1.print_list()
                 
