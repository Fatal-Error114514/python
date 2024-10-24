from sys import stdin

x,y = map(int,stdin.readline().split())

lst = []

for i in range(y):
    v1,v2,l = map(int,stdin.readline().split())
    lst.append([v1,v2,l])
lst.sort(key=lambda s:s[2])
print(lst)
