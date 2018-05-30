Write a program to validate if the input string has redundant braces?
Return 0/1

0 -> NO
1 -> YES
Input will be always a valid expression

and operators allowed are only + , * , - , /

Example:

((a + b)) has redundant braces so answer will be 1
(a + (a + b)) doesn't have have any redundant braces so answer will be 0


def redundant_braces(exp):
    """returns 1 if any redundant bracket is present else returns 0"""   
    cnt = 0  ## counter for elements popped from stack
    if '(' not in exp:
        return 0
    stack = []
    ## add elements in stack until closing bracket encountered
    for i in exp:
        stack.append(i)
        if i == ')' :
            stack.pop()  ## remove the last closing bracket
            while stack.pop() != '(':  ## check for last opening bracket
                cnt += 1
            if cnt  == 0 or cnt == 1:
                return 1
                
        cnt = 0  ## reset counter to zero
    return 0


assert redundant_braces("(a)") == 1
assert redundant_braces("(a+(a+b))") == 0   
assert redundant_braces("(a+b)")   == 0
assert redundant_braces("(a*b)+(b*c)") == 0
assert redundant_braces("(a+((a+b)))") == 1
assert redundant_braces("((a+(a+b)))") == 1
