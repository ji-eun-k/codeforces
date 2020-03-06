n1 = n = int(input())
count = newNum = 0

while True :
    n2 = (n1//10) + (n1%10)
    newNum = (n1%10) * 10 + n2 % 10
    n1 = newNum
    count += 1
    if n == newNum:
        break

print(count)