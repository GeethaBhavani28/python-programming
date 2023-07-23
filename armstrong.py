b=int(input())
summ=0
temp=b
while temp!=0:
    
    a=temp%10 
    c=a**3
    summ+=c
    temp=temp//10
    
if (summ==b):print("armstrong")
else:print("not an arm strong")
