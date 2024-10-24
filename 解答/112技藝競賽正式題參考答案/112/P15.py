from itertools import combinations


xs = eval(input())
print(len(set(map(sum, combinations(xs, 3)))))
