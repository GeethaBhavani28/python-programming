a,b=map(int,input().split())
es=0
os=0
for i in range(1,b+1):
    v=a*i
    if v%2==0:
        es+=v
    else:
        os+=v
print(es,os)
