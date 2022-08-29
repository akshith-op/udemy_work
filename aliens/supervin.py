n = int(input())
t = int(input())
for i in range(t):
    str = str(n)
    if str[0]%2 == 0:
        if str[1]%2==0:
            print(0)
        else:
            print(1)
    else:
        if str[0]%2 == 1:
            if str[1] <
