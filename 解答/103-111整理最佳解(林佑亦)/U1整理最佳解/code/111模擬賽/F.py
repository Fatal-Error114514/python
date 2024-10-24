from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n,m = map(int,Input().split())
    a,b,c = 1,1,1
    for _ in range(n-3):
        a,b,c = b,c,a+b+c
    print(str(c)[-m:])


#1 1 1 3 5 9 17