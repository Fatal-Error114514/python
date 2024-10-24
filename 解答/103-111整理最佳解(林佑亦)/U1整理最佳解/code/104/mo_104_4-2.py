from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b = Input().split(',')
    print(int(str(int(a[::-1]) + int(b[::-1]))[::-1]))

