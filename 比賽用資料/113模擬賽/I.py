s = input().split()
target = int(s[-1])
martix = eval(s[2].rstrip(','))
for i in martix:
    if target in i:
        print('true')
        break
else:
    print('false')