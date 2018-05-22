Problem :Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.

NOTE: All numbers can only have digits from the given set. 
Examples:
Input:
A = [ 0 1 5], B=  1  , C = 2  
Output:  2 (0 and 1 are possible)  
Input: A = 0 1 2 5  , B =  2  , C = 21  
Output:	  5 (10, 11, 12, 15, 20 are possible)
Constraints: 1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9
.............................................................................................................
Code :
.............................................................................................................
from itertools import combinations
def solve(A, B, C):
    if len(A) < B:
        return 0
    elif B > len(str(C)):
        #return permutations less than C
        return 0
            
    elif B < len(str(C)):
            #constraint is B
        new_list = list(combinations(A,B))
        print new_list
        return len(new_list)
                
            
            
    elif B == len(str(C)):
        #constraint is C 
        pass

print solve([0,1],1,5)
            
