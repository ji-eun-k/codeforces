n = int(input())
s = list(map(int, input().split()))
maxNum = -1001

for i in range(n):
    dp = max(dp+s[i], s[i])
    maxNum = max(dp, maxNum)

print(maxNum)