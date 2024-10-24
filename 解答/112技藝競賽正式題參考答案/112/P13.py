from itertools import permutations


xs = eval(input())
print(int(any(sum(perm[:3]) == sum(perm[3:]) for perm in permutations(xs))))
