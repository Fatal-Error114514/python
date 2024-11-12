from itertools import starmap
from operator import mul


print(sum(starmap(mul, zip(map(int, input().split()), [4, 6]))))
