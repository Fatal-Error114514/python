n = int(input())
for i in range(n // 2):
    for _ in range(n):
        print((i*n) * ' ' + '*')
    print((i*n) * ' ' + (n+1) * '*')
if n % 2:
    for _ in range(n):
        print((n//2) * ' ' + '*')