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
        high = 0
        low = 0
        start = 0
        x= len(A)
        max_length = 1
        for i in range(1,x):
            high = i
            low = i-1
            while high < x and low>0 and A[low] == A[high]:
                if high - low +1 >max_length:
                    start = low
                    max_length = high - low + 1
                high += 1
                low  -= 1
            high = i+1
            low = i-1
            while high < x and low>=0 and A[low] == A[high]:
                if high - low +1 >max_length:
                    start = low
                    max_length = high - low + 1
 
                high += 1
                low  -= 1
                
             
        return A[start : start+max_length]
            


print longestPalindrome('abb')
print longestPalindrome('aaaabbaaa')
print longestPalindrome('caba')
print longestPalindrome("abbcccbbbcaaccbababcbcabca") #this method fails for this input where two substrings of same size are encountered

