from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(Input())
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    print(a)


