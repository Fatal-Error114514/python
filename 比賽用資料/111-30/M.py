n = int(input())

for i in range(0, 2 ** n):
    g = i ^ (i >> 1)
    b = f'{g:b}'
    if len(b) < n:
        while len(b) != n:
            b = '0' + b
    print(b)

'''
2

00 ^ 00 = 00
01 ^ 00 = 01
10 ^ 01 = 11
11 ^ 01 = 10

'''