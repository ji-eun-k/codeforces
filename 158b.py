n = int(input())
s = list(map(int,input().split()))
count = 0
taxi = [0]*5
for i in s :
	taxi[i] += 1
count += taxi[4] + taxi[3] + taxi[2]//2

taxi[1]-=taxi[3]

if taxi[2]%2==1 :
	count+=1
	taxi[1]-=2

if taxi[1]>0 :
	count += (taxi[1]+3)//4

print(count)