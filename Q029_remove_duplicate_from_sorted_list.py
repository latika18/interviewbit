Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        stack = []
        cnt = 1
        curr = A   
        prev = A
        while A.next != None:
            prev.next = A
            cnt += 1
              
        for i in range(1, cnt//2 ):
            if curr.val == A.val:
                curr = curr.next 
                A.next = prev
                
            else: 
                return 0
        return 1
