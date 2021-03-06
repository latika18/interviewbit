Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Example:

Input : A : [4, 5, 2, 10, 8]
Return : [-1, 4, -1, 2, 2]

Example 2:

Input : A : [3, 2, 1]
Return : [-1, -1, -1]
CODE :
def prev_smaller(arr):
    new_stack = []
    status = False
    for i in range(len(arr)):
        for j in range(i,-1,-1):
            if arr[i]>arr[j]:
                status = True
                new_stack.append(arr[j])
                break
        if not status:
            new_stack.append(-1)
        status = False
    return new_stack
