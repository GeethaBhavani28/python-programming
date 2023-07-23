def conv_bin(n):
    if n==0:
        return " "
    quo=n//2
    rem=n%2
    return conv_bin(quo)+str(rem)
num=int(input())
rs=conv_bin(num)
print(rs)
