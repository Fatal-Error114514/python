from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    x,y = Input().split(', ')
    A = 0
    B = 0
    for i in range(len(x)):
        if(x[i] == y[i]):
            A += 1
        elif(x.count(y[i])):
            B += 1
    print(f'{A}A{B}B')
