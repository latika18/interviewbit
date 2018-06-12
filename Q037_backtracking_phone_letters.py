#Given a digit string, return all possible letter combinations that the number could represent.

#A mapping of digit to letters (just like on the telephone buttons) is given below.



#The digit 0 maps to 0 itself.
#The digit 1 maps to 1 itself.

#Input: Digit string "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#Make sure the returned strings are lexicographically sorted.

class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        d = {0:'0', 1:'1' , 2:'a b c',3:'d e f',4:'g h i',5:'j k l',6:'m n o',7:'p q r s',8:'t u v',9:'w x y z'}
        str_list = []
        ans =[]
        for i in A:
            i = int(i)
            if i in d:
                str_list.append(d[i])
        if len(str_list)== 1:
            return str_list
        
        ans =  [x+y for x in (str_list[0]) for y in (str_list[1])]
        return ans
        
