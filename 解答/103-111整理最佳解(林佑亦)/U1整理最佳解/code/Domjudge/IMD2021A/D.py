num = sorted(list(map(int,input().split())))
alpha = list(input())
for i in alpha:
    if(i == 'A'):
        print(num[0], end=' ')
    elif(i == 'B'):
        print(num[1], end=' ')
    else:
        print(num[2], end=' ')
print()
