You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.


code
def maxArr( A):
        
        max_sum_1= []
        max_sum_2 = []
        max_sum_3= []
        max_sum_4 = []
       
    
        
        
        
        for i, elem_i in enumerate(A):
            max_sum_1.append(elem_i - i)
            max_sum_2.append(elem_i + i)
        if max(max_sum_1)> max(max_sum_2):
            max_sum_12 = max(max_sum_1)
        else:
            max_sum_12 = max(max_sum_2)

        for j ,elem_j in enumerate(A):
            max_sum_3.append(elem_j + j)
            max_sum_4.append(elem_j - j)
        if max(max_sum_3)> max(max_sum_4):
            max_sum_34 = max(max_sum_3)
        else:
            max_sum_34 = max(max_sum_4)
                                   
        return max_sum_12 + max_sum_34

print maxArr([2,2,2])
print maxArr([2,-2,2])
print maxArr([-2,-2,-2])


