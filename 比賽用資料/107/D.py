from itertools import permutations

for _ in range(int(input())):
    lst = list(map(int, input().split(',')))
    n, k = lst.pop(0), lst.pop()
    per = list(permutations(lst, n))
    print(*per[k - 1], sep = '')