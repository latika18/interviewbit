#Add 1 to list s.t  list[1,2,3] o/p is [1,2,4] from interviewbit.com

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        Rev_A = A[::-1]
        i = 0
        while i <= len(A)-1:
            if Rev_A[i] != 9:
                Rev_A[i] +=1
                carry = 0
                break
            else:
                Rev_A[i] = 0
                carry = 1
            i += 1
        if carry == 1:
            Rev_A.append(1)
        while True:
            if Rev_A[-1]==0:
                Rev_A.pop()
            else:
                break
        return Rev_A[::-1]
        
            
    def __init__(self):
        self.list = []

A = Solution()
print A.plusOne([0,0,0,1,2,3])

