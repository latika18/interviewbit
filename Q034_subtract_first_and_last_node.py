Given a singly linked list, modify the value of first half nodes such that :

1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …

 NOTE :
If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. So, if L = 5, the first half refers to first 2 nodes.
If the length L of linked list is even, then the first half implies at first L/2 nodes. So, if L = 4, the first half refers to first 2 nodes.
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,

You should return 4 -> 2 -> 3 -> 4 -> 5
as

for first node, 5 - 1 = 4
for second node, 4 - 2 = 2
Try to solve the problem using constant extra space






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        fast = A
        slow = A
        prev = None
        cnt = 0
        if not A.next:
            return A
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            cnt += 1
        if fast:
            start = slow.next
        else:
            start = slow
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp

        firstA = A
        lastA = prev
        prev1 = prev      
        currA = A

        
        while cnt:
            currA.val = lastA.val - firstA.val
            firstA = firstA.next
            lastA = prev.next
            
            prev = prev.next
            
            currA = currA.next
            cnt -= 1
            
            
# reverse the list again
        new_prev =None
        while prev1:
            temp = prev1.next
            prev1.next = new_prev
            new_prev = prev1
            prev1 = temp
            
        
        return A

