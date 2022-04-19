def factor_count():
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc
n=int(input())
fc=factor_count()
if fc==2:
    print("prime")
else:
    print("not a prime")

 
