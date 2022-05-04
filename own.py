n,m=map(int,input().split())
i=2
hcf=1
while True:
    if n%i==0 and m%i==0:
       n=n//i
       m=m//i
       hcf=hcf*i
        
       
    else:
        i+=1
    if a<i or b<i:
         break
print(hcf*i)   
