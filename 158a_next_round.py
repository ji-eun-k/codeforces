n, k = map(int, input().split())
a = input().split()
count = 0

for i in a:
    if int(i) >= int(a[k-1]) and int(i)>0:
        count+=1

print(count)