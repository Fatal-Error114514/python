from sys import stdin

def Input():
    return stdin.readline().rstrip()

lst = []
for _ in range(int(Input())):
    lst.append(list(map(int,Input().split())))
lst.sort(key=lambda x:(x[1], x[2], -x[0]), reverse= True)

for i in lst:
    print(*i)

