Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]

import itertools
class Subsets:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, B):
        A = sorted(B)
        j = len(A)
        if not A:
            return A
        stack = [[]]
        self.append_sub(stack,A,j)
        return stack
        

    def append_sub(self,stack,A,j):
        if not A:
            return stack
       
        while j!= 0:
            stk = list(itertools.combinations(A, j))
            stk = map(list, stk)
            for i in stk:
                stack.append(i)
            
            j -= 1

        self.append_sub(stack,A[1:],j)
        stack.sort()
        return stack
