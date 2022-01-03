x=int(input('enter a number'))
n=int(input('enter root value'))
def root(x,n):
    temp=x**(1/n)
    return temp
ans=root(x,n)
print('the',n,'th root of',x,'is=',ans)
