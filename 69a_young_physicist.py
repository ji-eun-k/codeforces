n = int(input())
a = b = c = 0

for i in range(n):
    s = list(map(int, input().split()))
    a += s[0]
    b += s[1]
    c += s[2]

if a == b == c == 0:
    print('YES')
else:
    print('NO')