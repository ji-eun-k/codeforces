n = int(input())
while n:
    str = input()
    if len(str) > 10:
        print('%c%d%c' %(str[0],len(str)-2, str[len(str)-1]))
    else :
        print(str)
    n -= 1
