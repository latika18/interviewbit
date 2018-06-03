Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
Seen this question in a real interview before
#Code
def longestPalindrome(self, A):
        pal_string = ''
        x = len(A)
        y = 0 
        for i in range(0,x):
            for j in range(x,i-1,-1):
                new_str =  A[i:j]
                if new_str == new_str[::-1]:
                    if len(new_str) >= y:
                        y = len(new_str)
                        pal_string = new_str
                        
        return pal_string

print longestPalindrome('abb')
print longestPalindrome('aaaabbaaa')
print longestPalindrome('caba')
print longestPalindrome("abbcccbbbcaaccbababcbcabca") #this method fails for this input where two substrings of same size are encountered

