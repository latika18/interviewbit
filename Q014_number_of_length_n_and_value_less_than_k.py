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
from itertools import product
from itertools import ifilter
def solve(A, B, C):
    if A == [] or B > len(str(C)):
        return 0

    elif B < len(str(C)):
        #constraint is B
        if B == 1:
            new_list = A
            return len(new_list)
        else:
            new_list = list((product((''.join(str(i)for i in A)),repeat = B)))
            b = [''.join(num) for num in new_list]
            c = list(ifilter(lambda  x: x[0]!='0'  , b))
            return len(c)


    elif B == len(str(C)):
        #constraint is C 
        if B == 1:
            new_list = [i  for i in A if i< C]
            return len(new_list)
        else:
            new_list = list((product((''.join(str(i)for i in A)),repeat = B)))
            b = [''.join(num) for num in new_list]
            c = list(ifilter(lambda  x: x[0]!='0' and int(x) < C   , b))
            return len(c)
Test cases:

assert solve([2],5,51345) == 1
assert solve([],1,1) == 0
assert solve([ 2, 3, 5, 6, 7, 9 ],5,42950) == 2592
assert solve([0],1,5) == 1
assert solve([0,1,2,5],1,123) == 4
assert solve([0,1,5],1,2) == 2
assert solve([ 3 ],5, 26110) == 0
assert solve([0,1,2,5],2,21) == 5
