from math import gcd
from itertools import combinations

for _ in range(int(input())):
    lst = list(eval(input()))
    print(gcd(*lst))