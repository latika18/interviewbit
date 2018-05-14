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
        for i in range(1,x+1):
            if i not in  A:
                missing_num = i
            if A.count(i) == 2:
                repeated_num = i
                
        return repeated_num, missing_num
  
  
  
  
