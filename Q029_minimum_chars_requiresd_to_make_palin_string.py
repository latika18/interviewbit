You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2

def solve(self, A):
    
        if A[:] == A[::-1]:
            return 0
        count = 0
        while A[:] != A[::-1]:
            x = len(A)
            A = A[x-count-1] + A[:]
            count += 1
            
        return count
