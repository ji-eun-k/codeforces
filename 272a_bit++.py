n = int(input())
x = 0
while n != 0:
    operation = input()
    if operation[1] == '+':
        x += 1
    else:
        x -= 1
    n -= 1
print(x)
