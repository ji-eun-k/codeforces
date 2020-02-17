n = int(input())

isLucky = False

for i in range(1, n+1):
    m = str(i)
    isLucky = True
    for j in m:
        if j != '4' and j != '7':
            isLucky = False
    if n % i == 0 and isLucky == True:
        print('YES')
        exit()
print('NO')
