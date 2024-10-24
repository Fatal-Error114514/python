n = int(input())
lst = list(map(int,input().split()))
a = set()
for i in lst:
    a.add(i)
print(len(a))
print(*sorted(a))