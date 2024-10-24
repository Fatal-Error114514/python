from sys import stdin
from math import gcd

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = list(map(int,Input().split(',')))
    while(len(lst) > 1):
        lst[0] = gcd(lst[0],lst[1])
        lst.pop(1)
    print(*lst)