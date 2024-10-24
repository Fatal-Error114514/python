from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = Input()
while n:
    X = int(n)
    Y = int(Input())
    M = int(Input())
    print(pow(X, Y, M))
    Input()
    n = Input()



