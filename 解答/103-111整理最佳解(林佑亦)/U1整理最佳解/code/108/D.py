from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b,c = map(int,Input().split())
    print(pow(a, b, c))
