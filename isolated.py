from math import sqrt
def isolated_prime():
    sq=int(sqrt(n))
    for i in range(1,sq+1):
        if n%i==0:
         return False
    return True
n=int(input())
if (n+2 and n-2)!=p:
    print(True)
else:
    print(False)
