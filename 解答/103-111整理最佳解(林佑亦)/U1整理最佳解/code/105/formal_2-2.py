from sys import stdin
from math import gcd
from itertools import combinations

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = list(map(int,Input().split(',')))
    lst = [gcd(i[0], i[1]) for i in combinations(lst, 2)]
    print(max(lst))





