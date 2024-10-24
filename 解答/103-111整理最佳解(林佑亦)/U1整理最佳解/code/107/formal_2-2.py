from sys import stdin
from itertools import permutations

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    lst = list(map(int,Input().split(',')))[1:]
    k = lst.pop()
    lst = list(i for i in permutations(lst))
    print(*lst[k-1], sep='')

    