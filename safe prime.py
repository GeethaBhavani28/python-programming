from math import sqrt
def prime(n):
    sq=int(sqrt(n))
    for p in range(2,sq+1):
        if n%p==0:
            return False
        if n==2*p+1:
            return True
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
           
n=int(input())
print(prime(n))
