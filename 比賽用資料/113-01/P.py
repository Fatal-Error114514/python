from bisect import bisect_left
n = int(input())
lst = list(map(int,input().split()))
table = [lst[0]]
for i in range(n):
    if lst[i] > table[-1]:
        table.append(lst[i])
    elif lst[i] == table[-1]:
        continue
    else:
        table[bisect_left(table, lst[i])] = lst[i]
print(len(table))