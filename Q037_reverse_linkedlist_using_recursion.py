##Reverse a linked list using recursion.

##Example :
##Given 1->2->3->4->5->NULL,

##return 5->4->3->2->1->NULL.
class Solution:
    # @param A : string
    # @return a list of strings
def __init__(self):
        self.table={1:["1"],0:["0"],2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],
                    7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]    }
    def letterCombinations(self, A):
        ans=[]
        if len(A)==1:
            return self.table[int(A[0])]
        for j in self.table[int(A[0])]:
            temp=self.letterCombinations(A[1:])
            for i in temp:
                ans.append(j+i)
        return ans
