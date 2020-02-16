s = input()
word = ['h', 'e', 'l', 'l', 'o']
a = -1
for i in word:
    a = s.find(i, a+1)
    if a == -1:
        print('NO')
        exit()

print('YES')