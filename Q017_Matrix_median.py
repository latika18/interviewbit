Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.

For example,

Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5. So, we return 5.
Note: No extra memory is allowed.
 
 def find_median( A):
    """Returns the median value from given list"""
    list_new = []
    for i in A:
        for j in i:
            list_new.append(j)
    return (sorted(list_new)).pop(len(list_new)/2)
Test Cases:

assert find_median([[1,3,5],[2,5,9],[3,6,11]]) == 5
assert find_median([[0,1,1],[2,6,10],[3,5,9]]) == 3
assert find_median([[1,3,4,12,14],[1,6,9,10,15],[0,1,3,3,4]]) == 4

 
