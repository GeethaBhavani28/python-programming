def conv(n):
    if n==0:
        return" "
    d=n//8
    b=n%8
    return conv(d)+str(b)
num=int(input())
res=conv(num)
print(res)
