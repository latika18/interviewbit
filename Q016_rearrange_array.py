Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
Let us understand the above steps by an example array {3, 2, 0, 1}
In first step, every value is incremented by (arr[arr[i]] % n)*n
After first step array becomes {7, 2, 12, 9}. 
The important thing is, after the increment operation
of first step, every element holds both old values and new values. 
Old value can be obtained by arr[i]%n and new value can be obtained
by arr[i]/n.

In second step, all elements are updated to new or output values 
by doing arr[i] = arr[i]/n.
After second step, array becomes {1, 0, 3, 2}

Code:
 

def solve(arr):
    n = len(arr)
    # First step: Increase all values by (arr[arr[i]] % n) * n
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n
 
    # Second Step: Divide all values by n
    for i in range(0, n):
        arr[i] = int(arr[i] / n)
    return arr

print solve([ 4, 0, 2, 1, 3 ] )    
        
