from sys import stdin

def Input():
    return stdin.readline().rstrip()
#用combination會超時，因為有一些會重複到
n = int(Input())
coin = list(map(int,Input().split()))
lst = []
for i in coin:
    for j in range(len(lst)):
        lst.append(lst[j] + i)
    lst.append(i)
    lst = list(set(lst))
print(len(lst))
print(*lst)

