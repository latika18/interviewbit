Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        ptr_P = A
        ptr_Q = None
        ispal = False
        while ptr_P and ptr_P.next:
            ptr_P = ptr_P.next.next 
            ptr_Q = A
            ptr_Q.next = ptr_Q
            A = A.next
        if ptr_P:
            tail = A.next
        else:
            tail = A
            
        while ptr_Q:
            isPal = False
            if ptr_Q.val == tail.val:
                tail = tail.next
                ptr_Q = ptr_Q.next
                ispal = True
            
        if ispal :
            return 1
            
        else :
            return 0
