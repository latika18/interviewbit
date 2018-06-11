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

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        a  = sorted(A)
        stack = [[]]
        self.append_sub(stack,a)
        return stack
        

    def append_sub(self,stack,a):
        if not a:
            return stack
        curr = []
        stack.append(a[0])
        for i in a[1:]:
            curr = curr + [i]
            stack.append(curr)
            
        self.append_sub(stack,a[1:])
        return stack
