
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3

Code : 

def sqrt(A):
        low = 1
        high = A
        if A == 0 or A == 1:
            return A
        
        while low<=high:
            root =(low+high)/2
            if root*root == A:
                return root
            else:
                
                if A > (root*root):
                    low = root+1
                    ans = root
                    
                elif A < (root*root):
                    high = root-1
                    
        return ans
