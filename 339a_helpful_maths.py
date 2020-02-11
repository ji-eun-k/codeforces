s = input()
num1 = num2 = num3 = 0

for i in s:
    if i=='1':
        num1+=1
    elif i=='2':
        num2+=1
    elif i=='3':
        num3+=1

ss = '1+'*num1+'2+'*num2+'3+'*num3
print(ss[:-1])