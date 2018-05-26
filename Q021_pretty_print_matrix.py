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
    def swap_min(arr):
        arr
        k = min(arr)
        for i in range(len(arr)):
            if arr[i] == k:
                arr[i] = k+1       
        return arr                                                         
                     
    size_matrix = 2*A-1
    matrix = [[] for _ in range(size_matrix)]
    mid_pos = size_matrix // 2
    matrix[mid_pos]  = [ A-i for i in range(0,mid_pos)] + [A-i for i in range(mid_pos,-1,-1)]
    count =0
    j = 1
  
    while j <= mid_pos:## counter from 0 to mid_posv ## count adjacent to mid_pos
        
        ref_list = matrix[mid_pos]
        matrix[mid_pos-j] = matrix[mid_pos+j] = swap_min(ref_list)            
        j += 1
    
    return matrix
            
                                         


#print swap_min([1,1,22,3,4,2,5])

