from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b,x,y = map(int,Input().split())
    if([a, b] == [x, y]):
        print(0)
    elif(a == x or b == y) or (abs(a-x) == abs(b-y)):
        print(1)
    else:
        print(2)
