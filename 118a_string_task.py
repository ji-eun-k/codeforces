str = input()
for i in str:
    if i=='A' or i=='a' or i=='O' or i=='o' or i=='Y' or i=='y' or i=='E' or i=='e' or i=='U' or i=='u' or i=='I' or i=='i' :
        print("", end='')
    else :
        if i > 'a':
            print(".%c" %i, end='')
        else :
            print(".%c" %i.lower(), end='')