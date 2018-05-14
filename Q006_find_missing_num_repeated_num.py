You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

Code:
  
def repeatedNumber(A):
    missing_num = 0
    repeated_num = 0
    x = len(A)
    sum_of_num = 0
    sum_of_squares = 0
        
    for i in A:  
        sum_of_num += i
        sum_of_squares += i*i
       
    sum_of_num_actual = (x*(x+1))/2
    sum_of_squares_actual = ((x)*(x+1)*(2*x+1) ) / 6
    print sum_of_num_actual,sum_of_num
    print sum_of_squares_actual,sum_of_squares

    missing_num =  (((sum_of_squares_actual - sum_of_squares) /(sum_of_num_actual - sum_of_num))
                    +(sum_of_num_actual - sum_of_num))/2 
    repeated_num =  (((sum_of_squares_actual - sum_of_squares) /(sum_of_num_actual - sum_of_num))
                     -(sum_of_num_actual - sum_of_num))/2                  
    return repeated_num, missing_num

print repeatedNumber([1,2,3,4,5,2,6,8,9])

print repeatedNumber([1,2,3,4,5,16,6,8,9,10,11,12,13,14,15,16])
   
