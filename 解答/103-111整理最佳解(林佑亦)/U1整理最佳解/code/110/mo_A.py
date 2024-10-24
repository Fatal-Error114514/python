from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = Input()
while n:
    a,b,c = map(int,n.split())
    print(a*24+b*14+c*6)
    n = Input()
    