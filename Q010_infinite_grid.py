You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.
CODE :
 
 def cover_points(A, B):
    
    step = 0
    for k in range(1,len(A)):
        step_x =   abs(A[k]- A[k-1])
        step_y =   abs(B[k]- B[k-1])
        step += max(step_x,step_y)
      
    return step 

   print cover_points([ 4, 8, -7, -5, -13, 9, -7, 8 ],[ 4, -15, -10, -3, -13, 12, 8, -8 ])
print cover_points([ 2,3,4],[ 1,3,4 ])

