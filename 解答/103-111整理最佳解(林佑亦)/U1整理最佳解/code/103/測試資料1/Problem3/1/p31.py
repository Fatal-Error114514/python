from sys import stdin
from itertools import combinations
n = int(stdin.readline())
for h in range(n):
    a = list(map(int,stdin.readline().strip().split()))
    a.sort()
    ans = 0
    flower = list(combinations(a,5))
    for i in range(len(flower)):
        flower[i] = list(flower[i])
        for j in range(5):
            flower[i][j] -= j
        if set(flower[i]) == 1:
            ans = max(ans,7)
    four = a.copy()
    for i in range(6):
        four[i] %= 13
    if len(set(four))<=3:
        ans = max(ans,6)
    print(ans)
