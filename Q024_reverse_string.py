Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
Code:
 
def reverseWords(A):
    wordlist = []
    x = len(A)
    y = 0 ## len of previous string
    for i in range(x):
        if A[i] == ' ' :
            wordlist.append(A[y:i])
            y = i+1
    wordlist.append(A[y:x])
    return ' '.join(wordlist[::-1])

#print reverseWords("The sky is blue")
print reverseWords( "my name is latika agarwal")

# easier approach
def reverseWords(self, A):
        arr=A.split(" ")
        arr2=reversed(arr)
        return " ".join(arr2)

