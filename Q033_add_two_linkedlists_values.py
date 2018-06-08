You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

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
    def append(self, item):
        curr = self.head
        while curr.next:
            curr = curr.next
        node = ListNode(item)
        curr.next = node
    def addTwoNumbers(self, A, B):
        carry = 0
        x = 0
        sum_AB = 0
        currA =A
        currB = B
        
        while currA and currB:
            
            sum_AB = currA.val + currB.val + carry
            x  = sum_AB - 10 
            if x >= 0:
                carry = 1
                currA.val = x
            else:
                carry = 0
                currA.val = sum_AB
            currA= currA.next
            currB= currB.next
        if not currA and not currB and not carry:
            return A

        if currA:
            while currA:
                currA.val += carry
                x  =  currA.val - 10 
                if x >= 0:
                    carry = 1
                    currA.val = x
                else :
                    carry = 0
            
                currA= currA.next
            
        
        if currB:
            currA = currB
            curr_new = A
            while curr_new.next:
                curr_new = curr_new.next
            curr_new.next = currA
            while currB and currA:
                currB.val += carry
                x  =  currB.val - 10 
                if x >= 0:
                    carry = 1
                    currB.val = x
                else:
                    carry = 0
                currB = currB.next
                currA = currB
           
            
        if carry:
            print "are y happy"
            self.append(carry)
        return A
            

    def print_list(self):
        temp = self.head
        while(temp):
            print temp.val
            temp = temp.next
              
    
       
##llist = Solution([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7])
##print llist.reverseList(1)
B = Solution([ 9,9,3,3])
A = Solution([1,1,1,1])
##B = Solution([ 9,9,9])
##A = Solution([1])
##print A.print_list()
##print B.print_list()
##llist = Solution([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7])
##print llist.reverseList(1)
##A = Solution([1])
##B = Solution([1,2,3])
##print A.print_list()
##print B.print_list()
##                 
##
A.addTwoNumbers(A.head, B.head)
print A.print_list()
