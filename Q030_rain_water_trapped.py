Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example :

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Rain water trapped: Example 1
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
http://i.imgur.com/0qkUFco.png

 def trap(self, A):
        high = 0
        next_high = 0
        water_trapped = 0
        j = 0
        for i in range(len(A)):
            if A[i] > high:
                high = A[i]
                j = i
                while A[j] <= high and j < len(A)-1:
                    water_trapped += high - A[j]
                    j += 1
                next_high = A[j]
            i = j
               
        return water_trapped
