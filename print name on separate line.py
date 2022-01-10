name=input('enter your name')
times=int(input('enter number of times to repeat'))
print('print on separate line')
print('') if times<=0 else print(times * (name+('\n')))
