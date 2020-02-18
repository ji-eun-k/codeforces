n = int(input())
c = m = 0
for i in range(n):
    a = list(map(int, input().split()))
    c = c - a[0] + a[1]
    if c > m:
        m = c

print(m)
