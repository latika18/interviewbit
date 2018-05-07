#Task : Find out the maximum sub-array of non negative numbers from an array. The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid. Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

#Note: If there is a tie then compare the segment length's and return segment which has maximum length.

#Code:

import pdb
import itertools

def maxset(array):
    """Returns maximum sub array of non-negative numbers"""
    sum = 0
    max_sum = 0
    current_sum = 0
    start = 0
    stop = 0
    max_array = array[start:stop]
    count = 0
    
    
    for i in range(len(array)):
        if array[i] >= 0:
            sum = sum + array[i]
            current_sum = sum
            stop = stop+1
            if max_sum < current_sum:
                max_sum = current_sum
                if max_array < array[start:stop]:
                    max_array = array[start:stop]
                
            elif max_sum == current_sum:
                if len(max_array)< len(array[start:stop]):
                    max_array = array[start:stop]
                      
        else :
            
            start = i+1
            stop = start
            sum = 0
            current_sum = 0
           
    return max_array

