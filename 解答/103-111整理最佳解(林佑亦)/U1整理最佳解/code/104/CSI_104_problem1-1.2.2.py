from sys import stdin
from itertools import combinations
n = int(stdin.readline())
ans = list(map(int,stdin.readline().split(",")))
for h in range(n):
    a = list(map(int,stdin.readline().split(",")))
    lis=list(combinations(a,5))
    s = []
    for i in lis:
        x = len(set(i)&set(ans))
        s.append(x)
    for i in range(2,6):
        if i <5:
            print(s.count(i),end=",")
        else:
            print(s.count(i))
