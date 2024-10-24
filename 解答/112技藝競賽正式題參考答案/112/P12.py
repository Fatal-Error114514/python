from itertools import groupby


print(sum(max(0, len(list(g)) - 2) for _, g in groupby(input())))
