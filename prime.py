from math import sqrt
def factor_count():
    if n==1:
        return 1
    fc=2
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            fc+=2
    if n==sq*sq:
        fc-=1
    return fc
 
n=int(input())
fc=factor_count()
print(fc)
