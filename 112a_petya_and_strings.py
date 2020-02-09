str1 = input().lower()
str2 = input().lower()
i = 0
while i < len(str1):
    if str1[i] < str2[i]:
        print('-1')
        break
    elif str1[i] > str2[i]:
        print('1')
        break
    elif str1[i] == str2[i] and i == len(str1) - 1:
        print('0')
    i += 1
