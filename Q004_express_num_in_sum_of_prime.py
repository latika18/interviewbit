import math
def list_prime(A):
    
   bool_a = [True for i in range(2,A+3)] # creates boolean list of indeex
    for  i in range(2, int(math.sqrt(A))+1): # 
        if bool_a[i]:
            for j in range( i * i, A +1 , i):
                if bool_a[j]:
                    
                    bool_a[j] = False;
    
            
        
    primes = []
    
    for i in range(2,A):
        if bool_a[i]:
            primes.append(i)
    return primes




def primesum(A):
    solution_set = []

    for i in (list_prime(A)):
        for j in (list_prime(A)):
            if i + j == A:
                solution_set.append((i,j))
                
                break


    return min(solution_set)

print primesum(104)

print primesum(1048)
print list_prime(1048574)








