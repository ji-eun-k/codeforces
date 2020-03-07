n = int(input())
so = list(map(int, input().split()))
count = 0

for i in so:
    isSo = 1
    for j in range(2, i):
        if i % j == 0:
            isSo = 0
    if i <= 1:
        isSo = 0
    if isSo == 1:
        count += 1
print(count)