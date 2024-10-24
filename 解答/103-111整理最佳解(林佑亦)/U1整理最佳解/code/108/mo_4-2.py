from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b = map(int,Input().split())
    b = max(a - b, b)
    total = 1
    for i in range(a, b, -1):
        total *= i
    for i in range(2, a-b+1):
        total //= i
    print(total)

