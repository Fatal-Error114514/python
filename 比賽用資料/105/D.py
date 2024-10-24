from math import gcd
from itertools import combinations

for _ in range(int(input())):
    lst = list(map(int,input().split(',')))
    print(max(gcd(i[0], i[1]) for i in combinations(lst, 2)))