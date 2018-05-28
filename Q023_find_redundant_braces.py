Write a program to validate if the input string has redundant braces?
Return 0/1

0 -> NO
1 -> YES
Input will be always a valid expression

and operators allowed are only + , * , - , /

Example:

((a + b)) has redundant braces so answer will be 1
(a + (a + b)) doesn't have have any redundant braces so answer will be 0


def braces(A):
    stack = []
    status = False
    cnt = 0
    e_cnt = 1
    exp_cnt =0 
    i = 0
    while i < len(A):
        while A[i]  != ')':
            stack.append(A[i])
            i += 1
        i += 1
        
        for _ in range(len(stack)):
            k = stack.pop()
            print k
            if k == '(':
                break
        if stack == []:
            return 0
        i += 1

    if stack.pop() == '(':
        return 1
    else:
        return 0


print braces("((a+b))")
"(a/b)+(b*d)+(a*a)+a"


