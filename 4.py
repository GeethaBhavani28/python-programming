marks,total=map(int,input().split())
percentage=(marks*100)/total
if percentage>75:
    print("a+",end=' ')
elif percentage>60:
    print("a",end=' ')
elif percentage>50:
    print("b",end=' ')
else:
    print("c",end=' ')
