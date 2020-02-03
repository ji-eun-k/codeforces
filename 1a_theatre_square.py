n, m, a = map(int, input().split())
if n % a == 0:
    temp1 = n//a
else:
    temp1 = n//a + 1

if m % a == 0:
    temp2 = m//a
else:
    temp2 = m//a + 1

print(temp1*temp2)
