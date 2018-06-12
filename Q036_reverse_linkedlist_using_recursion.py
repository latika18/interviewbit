# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    
    def Reverse_List_Recursion(self, p):
        if p.next is None:
            self.head = p
            return
        self.Reverse_List_Recursion(p.next)
        q = p.next
        q.next = p
        p.next = None
        
    def reverseList(self, p):
        self.head = p
        self.Reverse_List_Recursion(p)
        return self.head
        
