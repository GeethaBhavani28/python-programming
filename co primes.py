from math import sqrt
def gcd(a,b):
    while b:
        if a>b:
            a,b=b,a
        b=b%a
        return a

n1,n2=map(int,input().split())
if (gcd(n1,n2)==1):
    print("co primes")
else:
    print("not a coprimes")
