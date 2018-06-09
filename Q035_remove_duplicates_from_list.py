Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A.next is None:
            return A
       
        curr = A        
        result = A
        while curr.next:
            
            if curr.val == curr.next.val:
                curr = curr.next.next
                result = curr
            while result.val == curr.val:
                curr = curr.next
            result.next  = curr
            result = result.next
        return result
                
        
