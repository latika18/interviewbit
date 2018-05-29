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
    x = ['+','-' ,'/','*']
    
    
    if '(' not in A:
        return 0
    stack = []
    for i in A:
        stack.append(i)
           
        if i == ')':
            if not any(i in stack for i in x):
                return 1
            stack.pop()
            if stack.pop() == '(':
                return 1
            for _ in range(len(stack)):
                k = stack.pop()
                if k == '(':
                    break

    return 0
##print braces("(a)")   
##print braces("(a+b)")   
print braces("(a*b)+(b*c)")
   


