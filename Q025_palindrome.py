

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
CODE :
def isPalindrome(self, A):
        A = A.upper()
        B = []
        for i in A:
            if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                B.append(i)
        C = []
        for i in A[::-1]:
            if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                C.append(i)
        if B == C:
            return 1
            
        else:
            return 0
            
 FASTER APPROACH:           
 def isPalindrome(self, A):
        bare_string = A.translate(None,string.punctuation).replace(" ","").lower()
        on_string = bare_string[::-1]
        
        if on_string == bare_string:
            return 1
        else:
            return 0            
