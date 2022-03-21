num=int(input())
while num:
     if num%3==0 and num%5==0:
        break
     print(num,end=' ')
     num-=1
else:
    print("hai")
