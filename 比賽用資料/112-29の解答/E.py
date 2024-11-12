from functools import partial
from operator import lt


print(next(filter(partial(lt, int(input())), (2 ** i for i in range(21)))) // 2)
