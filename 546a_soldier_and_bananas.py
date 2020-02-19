num = list(map(int, input().split()))
price = 0

for i in range(num[2]):
    price = price + num[0] * (i+1)

if price - num[1] <= 0:
    print(0)
else:
    print(price-num[1])