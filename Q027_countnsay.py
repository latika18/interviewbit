The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11
#CODE
def countAndSay(self, A):
        string = '11'
        cnt = 0
        new_string = ''
        if A == 1:
            return "1"
        while A != 2:
            cnt += 1
            for i in range(len(string)):
                if i+1 != len(string):
                    if string[i] == string[i+1]:
                        cnt += 1
                    else:
                        new_string += new_string + str(cnt)+string[i] 
                else:
                    new_string = new_string + str(cnt) +string[i]
            cnt = 0
            A -= 1
            string = new_string 
            new_string = ''
        return string
