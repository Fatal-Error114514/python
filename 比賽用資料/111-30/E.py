count = [0 for i in range(int(input()))]
lst = list(map(int,input().split()))
n = set()
for i in lst:
    count[lst.index(i)] += 1
    n.add(i)
for i in sorted(n):
    print(i,count[lst.index(i)])