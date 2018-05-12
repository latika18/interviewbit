You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.


# -*- coding: utf-8 -*-
##Maximum Absolute Difference
##You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
##f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
##|A[i] - A[j]| + |i - j| = -A[i]+ A[j] - i + j = -(A[i]+ i)+( A[j] + j)
##|A[i] - A[j]| + |i - j| = -A[i]+ A[j] + i - j = -(A[i] - i) + (A[j]-j)

##|A[i] - A[j]| + |i - j| = A[i]- A[j] - i + j = (A[i] - i) - (A[j] -j) 
##|A[i] - A[j]| + |i - j| = A[i]- A[j] + i - j = (A[i] + i) - (A[j] + j)
##Cases 1 and 4 are same
##cases 2 and 3 are same
##For example,
##
##A=[1, 3, -1]
##
##f(1, 1) = f(2, 2) = f(3, 3) = 0
##f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
##f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
##f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
##
##So, we return 5

def max_abs_diff(array):
    """ returns sum of absolute difference of values and corresponding indices of an array"""
    max1=[]#array to store maximum values given by A[i] + i
    min1=[]#array to store minimum values given by A[i] + i
    max2=[]#array to store maximum values given by A[i] - i
    min2=[]#array to store minimum values given by A[i] - i
                
    for i, elem in enumerate(array):
      
        max1.append(elem + i)  
        min1.append(elem + i)
        max2.append(elem - i)
        min2.append(elem - i)
                    
    return max(max(max1) - min(min1) , max(max2)-min(min2))
         
print max_abs_diff([2,2,2]) == (2)
print max_abs_diff([2,-2,2])== (5)
print max_abs_diff([-4,-2,-3,-4,-5]) == (6)
print max_abs_diff([-1]) == (0)
print max_abs_diff([-5, 1, -3, 7, -1, 2, 1, -6, 5]) == (18)
print max_abs_diff( [6, -3, -2, 7, -5, 2, 1, -7, 6]) == (20)
print max_abs_diff([-5, -2, -1, -4, -7]) == (8)
