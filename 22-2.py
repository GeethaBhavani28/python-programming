a,b=map(int,input().split())
n=a

for i in range(1,2*b+1):
    if i<=b:
     print(a,i,a*i)
    else:
        i-=n
        print(n,i,i*n)
   
