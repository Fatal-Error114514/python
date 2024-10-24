from sys import stdin

def Input():
    return stdin.readline().strip()

n = Input()
while n:
    lst = list(map(int,n.split()))
    limit = lst.pop(0)
    del lst[0]
    table = [0 for i in range(limit+1)]

    #動態規劃dp
    for i in lst:
        for j in range(limit, i-1, -1):
            table[j] = max(table[j], i + table[j-i])
    print(table[-1])
    n = Input()
