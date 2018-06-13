Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]


def combine(A, B):
    alist = []
    i = 0
    
    while i <= A and A>=B:
       
        append_num(alist,i,A,B)
        i +=1
        
    return alist
    
def append_num(alist,i,A,B):
    if i == A:
        return alist
    i = i+1
    j = i
    a = [i]
    while i <= A:
        while B>j:
            j = j+1
            a = a + [j]
            
        alist.append(a)
        i = j
    return alist


print combine(4,2)
