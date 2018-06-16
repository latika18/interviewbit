Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.

Example :

S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).





class Solution:
    # @param S : string
    # @param T : string
    # @return a string
    def minWindow(self, S, T):
        from collections import defaultdict
        count_dict = defaultdict(int)
        
        for c in T:
            count_dict[c] += 1
        
        st = 0
        end = 0
        remaining = len(T)
        min_st = 0
        min_len = len(S) + 1
        
        n = len(S)
        while end < n:
            if count_dict[S[end]] > 0:
                remaining -= 1
            
            count_dict[S[end]] -= 1
            end += 1
            
            while remaining == 0:
                if end - st < min_len:
                    min_len = end - st
                    min_st = st
            
                count_dict[S[st]] += 1
                if count_dict[S[st]] > 0:
                    remaining += 1
                st += 1
        
        if min_len == len(S) + 1:
            return ""
        
        return S[min_st:min_st+min_len]
