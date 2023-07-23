n=int(input())
while(n!=0):
    d=n%10
    if (d!=0 and d!=1):
        print("not a binary")
        break
    n=n//10
    if n==0:
        print("binary")
'''num = int(input("please give a number : "))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
        print("num is not binary")
        break
    num=num//10
    if num==0:
        print("num is binary") '''
     

     
