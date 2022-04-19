n=int(input())
if isprime(n):
    left=n-1
    while True:
        if isprime(left):
            break
         if left%2:
             left-=2
         else:
             left-=1
    right=n+2
    while True:
        if isprime(right):
            break
        right+=2
    if n*n>left*right:
        print(True)
    else:
        print(False)
                 
