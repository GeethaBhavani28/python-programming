from math import sqrt
def sum_factors():
    es=0
    os=0
    sq=int(sqrt(n))
    for i in range(1,sq+1):
        if n%i==0:
            if i%2:
                os+=i
            else:
                es+=i
            if (n//i)%2:
                os+=n//i
            else:
                es+=n//i
    if n==sq*sq:
        if sq%2:
            os-=sq
        else:
            es-=sq
    return os,es
             
n=int(input())
res=sum_factors()
print(res)

