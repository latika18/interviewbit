Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.

def pow( x, n, d):
    """returns remainder of x ^ n / d """
    def power(x,n):
        """returns x ^ n """        
        x = abs(x)
        if n == 0:
            return 1
        elif n == 1 :
            return x
        else:
            for i in range(1,n):
                x *= x
                return x
   
    def mod(x,d):
        """returns remainder of x /d""" 
        x = abs(x)
        if x == 1:
            return d-1
        else:
            y = x/d
            z = x - y*d
            return z
    
    return mod(power(x,n),d)
    
assert pow( -1, 1, 20) == 19
print pow( -1, 2, 20) == 


print pow(71045970,41535484,64735492)
