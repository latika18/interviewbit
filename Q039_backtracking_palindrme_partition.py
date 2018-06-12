Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")

Code : 
def partition(A):
    list_str = [[i for i in A]]
    j = 0
    recurse(list_str,j,A)
    return list_str
    
def recurse(list_str, j,A):
    if j == len(A):
        return list_str
    
    a = list_str[0][j]
    print j 
    for i in range(j+1,len(list_str[0])):
        a = a + str(list_str[0][i])
        if a == a[::-1]:
            if a == A:
                list_str.append([a])
            
            
            break
    print list_str
    j = j+1
    recurse(list_str,j,A)
    return list_str    
    
    

print partition("aab")
print partition("efe")
