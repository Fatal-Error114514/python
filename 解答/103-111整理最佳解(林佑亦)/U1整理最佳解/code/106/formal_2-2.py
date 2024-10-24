from itertools import permutations
from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    x,y,z = map(int,Input().split(','))
    A = 0
    B = 0
    lst = [i for i in permutations(str(x))]
    y = lst[y-1]
    z = lst[z-1]
    for i in range(len(y)):
        if(y[i] == z[i]):
            A += 1
        elif(y.count(z[i])):
            B += 1
    print(f'{A}A{B}B')
