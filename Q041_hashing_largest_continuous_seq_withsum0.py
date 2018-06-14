#Find the largest continuous sequence in a array which sums to zero.

#Example:
#Input:  {1 ,2 ,-2 ,4 ,-4}
#Output: {2 ,-2 ,4 ,-4}
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        end =0
        
        for i in range(0,len(A)):
            sum_0 = A[i]
            start =i 
            for j in range(i+1,len(A)):
            
                sum_0 += A[j]
                if sum_0 == 0:
                    end = j
                    break
            
            
        return A[start:end+1]       
