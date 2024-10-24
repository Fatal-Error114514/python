from collections import Counter
from itertools import starmap
from operator import ne


s1, s2 = input(), input()

if Counter(s1) == Counter(s2):
    res = sum(starmap(ne, zip(s1, s2)))
    print(int(2 in Counter(s1) if res == 0 else res == 2))
else:
    print(0)
