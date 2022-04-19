from math import sqrt
def is prime(n):
    if n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1)
     if n%i==0:
         return false
    return True
n=int(input())
if (isprime(n) and not(isprime(n+2)and not isprime(n-2)):
    print("true")
else:
    print("false")
