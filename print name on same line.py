name=input('enter name')
times=int(input('number of times to repeat'))
print("print on same line")
print('') if times<=0 else print((name+' ' )*times)
