from itertools import permutations

num = list(range(1, int(input()) + 1))
for i in reversed(list(permutations(num))):
    print(*i, sep = '')