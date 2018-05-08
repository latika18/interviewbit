import math
def list_prime(A):
    
    list_A = [i for i in range (2,A) ]
        
    for i in range(2, int(math.sqrt(A))):
        for j in (list_A):
            if j % i == 0 and i != j:
                list_A.remove(j)
    return list_A


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








