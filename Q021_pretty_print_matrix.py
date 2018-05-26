Print concentric rectangular pattern in a 2d matrix. 
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
Example 2:

Input: A = 3.
Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
import pdb
    def prettyPrint(A):
        ##    m x n matrix, rows x column
        n = m = 2*A -1
        k = 0 # row start counter
        l = 0 # column start counter
        i = 0 # iterator

        matrix = [[0 for _ in range(n)] for _ in range(m)]
    
    
        while k < m and l < n :
            #insert the first row
            for i in range(l,n) :
                if matrix[k][i] == 0:
                    matrix[k][i] = A  # row index constt, insert in columns
            
            k += 1         # first row printed, so increment start index

            #insert the last column
            for i in range(k,m) :
                if matrix[i][n-1]==0:
                    matrix[i][n-1] = A   # column index constt, insert in rows
            n -= 1                          # last column printed, so decrement num of columns
        
            #insert the last row
            if (k<m):
                for i in range(n-1 ,l-1,-1):
                    if matrix[m-1][i] == 0:
                        matrix[m-1][i] = A   # row index constt, insert in columns
            m -= 1                           # last row printed, so decrement num of rows
            
            #insert the first column
            if (l<n):
                for i in range(m-1,k-1,-1):
                    if matrix[i][l] == 0:
                        matrix[i][l] = A # column index constt, insert in rows
            l += 1      # first column printed, so increment start index
            A -= 1
        
        return matrix 
