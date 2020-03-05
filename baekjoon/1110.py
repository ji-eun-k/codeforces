n1 = n = input()
count = new = 0

while int(n) != int(new):
    if int(n1) < 10:
        n1 = '0'+n1
    n2 = int(n1[0])+int(n1[1])
    n2 = str(n2)
    if int(n2) < 10:
        n2 = '0'+n2
    new = n1[1]+n2[1]
    print(new)
    n1 = new
    count += 1

print(count)