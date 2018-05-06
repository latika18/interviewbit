#Task : Find out the maximum sub-array of non negative numbers from an array. The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid. Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

#Note: If there is a tie then compare the segment length's and return segment which has maximum length.

#Code:

def maxset(array):
"""Returns maximum sub array of non-negative numbers"""
sum = 0
current_sum = []
count = 0
sub_array = []
sub_array_list = []

for i in range(len(array)):
    if array[i] >= 0:
        sum = sum + array[i]
        sub_array.append(array[i])

    else:
        current_sum.append(sum)
        sub_array_list.append(sub_array)
        sum = 0
        sub_array = []
        count += 1

if count == 0:
    return sub_array
max_sum = max(current_sum)    
if max_sum > sum:
    i= current_sum.index(max_sum)
    return sub_array_list[i]
elif max_sum < sum:
    return sub_array
elif max_sum == sum:
    if len(sub_array) > len(max(sub_array_list,key=len)):
        return sub_array
    else:
        return max(sub_array_list,key=len)
#Test cases :

def main():        
    print maxset([ 336465782, -278722862, -2145174067, 1101513929, 1315634022, -1369133069, 1059961393, 628175011, -1131176229, -859484421 ])
    print maxset( [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ] )
    print maxset( [ 1, 2, 5, -7, 2, 5 ] )
    print maxset( [ 1, 2, 5, -7, 2, 5 ] )
    print maxset( [ 222])
    print maxset( [ 1, 1])
    print maxset( [  3, -1, 1, 1, 1, -1, 3])   
if __name__ == '__main__':
    main()
