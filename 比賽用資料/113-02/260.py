from itertools import combinations

n = int(input())
lst = set(range(1, n + 1))
ok = False
for i in range(len(lst) - 1):
    for j in combinations(lst, i):
        if sum(j) == sum(lst) - sum(j):
            ok = True
            lst = lst - set(j)
            print('YES', str(min(sorted(lst), sorted(j),key = lambda x: len(x))).replace(' ',''), str(max(sorted(lst), sorted(j), key = lambda x: len(x))).replace(' ', ''), sep = ',')
    if ok:
        break
else:
    print('NO')
