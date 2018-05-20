Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)


def maximumGap(self, A):
        gap = 0
        A = list(map(list, enumerate(A)))
        x = A[0]
    
    
        for item in A:
            item[0],item[1] = item[1], item[0]
            a = sorted(A)
            minindex = 0
            maxindex = 0
              
        k = a.index(x)
        
        for i in range(k,len(a)):
            
            if a[i][1] > maxindex:
                maxindex = a[i][1]
               
        gap = maxindex
                
        
        
        return gap
