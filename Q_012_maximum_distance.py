




def maximumGap(self, A):
        gap = 0
        
        for i in range(len(a)-1):
            for j in range(i, len(A)):
                if A[i] <= A[j]:
                    gap_new = j - i
                    if gap < gap_new:
                        gap = gap_new
        
        return gap
