#Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
#If such an integer is found return 1 else return -1.

 def solve(A):
        A = sorted([x for x in A if x >= 0], reverse=True)
        A = list(map(list, enumerate(A)))
        for i, v in A[1:]:
            if v == A[i-1][1]:
                A[i][0] = A[i-1][0]
        return 1 if any(v == i for i, v in A) else -1

Test Cases      
print solve([4,7,8,9,11])
print solve([-4, -2, 0, -1, -6 ])
print solve([-4, -2, -1, -6 ])
print solve([6,7,5 ])

print solve([ -1, -2, 0, 0, 0, -3 ])
print solve([ 4, -9, 8, 5, -1, 7, 5, 3 ])
print solve ([ -4, 7, 5, 3, 5, -4, 2, -1, -9, -8, -3, 0, 9, -7, -4, -10, -4, 2,
               6, 1, -2, -3, -1, -8, 0, -8, -7, -3, 5, -1, -8, -8, 8, -1, -3, 3,
               6, 1, -8, -1, 3, -9, 9, -6, 7, 8, -6, 5, 0, 3, -4, 1, -10, 6, 3,
               -8, 0, 6, -9, -5, -5, -6, -3, 6, -5, -4, -1, 3, 7, -6, 5, -8, -5,
               4, -3, 4, -6, -7, 0, -3, -2, 6, 8, -2, -6, -7, 1, 4, 9, 2, -10, 6,
               -2, 9, 2, -4, -4, 4, 9, 5, 0, 4, 8, -3, -9, 7, -8, 7, 2, 2, 6, -9,
               -10, -4, -9, -5, -1, -6, 9, -10, -1, 1, 7, 7, 1, -9, 5, -1, -3, -3,
               6, 7, 3, -4, -5, -4, -7, 9, -6, -2, 1, 2, -1, -7, 9, 0, -2, -2, 5,
               -10, -1, 6, -7, 8, -5, -4, 1, -9, 5, 9, -2, -6, -2, -9, 0, 3, -10,
               4, -6, -6, 4, -3, 6, -7, 1, -3, -5, 9, 6, 2, 1, 7, -2, 5 ])
