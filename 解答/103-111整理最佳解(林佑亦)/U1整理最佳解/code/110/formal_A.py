from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = Input()
while n:
    a,b = map(int,n.split())
    print(4*a + 6*b)
    n = Input()
