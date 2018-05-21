Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)


def maximumGap(self, A):
        def maximum_gap( A):
    """find maximum gap between index(j -i ) with  A[i] <= A[j]"""
    gap = 0
    A = list(map( list,enumerate(A))) # get list of [index,value]
    for item in A:
        item[0],item[1] = item[1], item[0] # swap index with value
    a = sorted(A)  # sort list A as per values

    max_index = a[0][1] # initialise max_index to first index in sorted list
    min_index = a[0][1] # initialise min_index to first index in sorted list

    for v,i in a:
        if i > max_index:  # if current > max_index, set max to current
            max_index = i
        if i < min_index:  # if current < min_index, set min to current
            min_index = i
            max_index = i  # reset max to current

        gap_new = max_index - min_index  # find the maximum gap
        if gap < gap_new:
            gap = gap_new

    return gap
Test cases:

print maximum_gap([-1,-1,2])  == 2
print maximum_gap([1,3,5,7,2,4,10])  ==  6
print maximum_gap([3,2,1]) == 0
print maximum_gap([3,2,1,4]) == 3
print maximum_gap([2,2,1,4,3])  == 4
print maximum_gap([ 0,1,2,3])  == 3
print maximum_gap([ 100,100,100,100,100])  == 4
