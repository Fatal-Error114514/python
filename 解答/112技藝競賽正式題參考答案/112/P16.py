from itertools import starmap
from operator import eq


s1, s2 = input(), input()

if not s2.isnumeric() or len(s2) != 4 or len(set(s2)) < 4:
    print('0A0B')
else:
    a = sum(starmap(eq, zip(s1, s2)))
    b = sum(c in s1 for c in s2) - a
    print(f'{a}A{b}B')
