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
