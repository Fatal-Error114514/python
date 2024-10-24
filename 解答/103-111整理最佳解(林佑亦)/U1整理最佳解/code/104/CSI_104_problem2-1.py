from itertools import permutations
from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst,a,b = map(int,Input().split(','))
    lst = [list(i) for i in permutations(str(lst))]
    print(int(''.join(lst[a-1])) + int(''.join(lst[b-1])))
