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
def longestPalindrome(A):
        for i in range(len(A)):
            print A[i+1:]
            print A[:i:-1]
            if A[i+1:] == A[:i:-1]:
                return A[i+1:]



print longestPalindrome('abb')

