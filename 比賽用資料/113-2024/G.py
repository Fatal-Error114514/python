m, n = map(int,input().split())
a = []
for i in range(m):
    a.append(list(map(int,input().split())))
for i in list(zip(*a)):
    print(*i)