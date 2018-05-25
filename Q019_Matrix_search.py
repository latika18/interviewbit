Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem

Code:
  
def searchMatrix(self, A, B):
    status = 0
    for item in A:
        if B >= item[0] and B <= item[(len(item)-1)]:
            if B in item :
                status = 1
                
    if status :
        return 1
    else:
        return 0 
        
