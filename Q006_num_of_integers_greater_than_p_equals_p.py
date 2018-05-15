#Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
#If such an integer is found return 1 else return -1.

 def solve(self, A):
        p = -1
        status = False
        for i in range(1,len(A)):
            if i == A[i+1]:
                status = True
        
        if status:
            p = 1
        
        return p
