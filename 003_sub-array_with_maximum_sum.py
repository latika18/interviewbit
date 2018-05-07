def maxSubArray(A):
    start ,stop = 0 , 0
    curr = 0
    max_sum = A[0]
    current_sum = 0
    for i in range(len(A)):
        current_sum +=  A[i]
        
        if max_sum < current_sum:
            max_sum = current_sum 
            start = curr
            stop = i
        if current_sum < 0:
            current_sum = 0
            curr = i + 1
         
    return max_sum , A[start:stop]

print maxSubArray([-2,-3,-4,-5])
    

print maxSubArray([-1])
print maxSubArray([-5, 1, -3, 7, -1, 2, 1, -4, 6])
print maxSubArray([-5, 1, -3, 7, -1, 2, 1, -6, 5])
print maxSubArray( [6, -3, -2, 7, -5, 2, 1, -7, 6])
print maxSubArray([-5, -2, -1, -4, -7])
print maxSubArray( [4, 1, 1, 4, -4, 10, -4, 10, 3, -3, -9, -8, 2, -6, -6, -5, -1, -7, 7, 8])
print maxSubArray([4, -5, -1, 0, -2, 20, -4, -3, -2, 8, -1, 10, -1, -1 ])
