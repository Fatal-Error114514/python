from itertools import product

lst1 = []
lst2 = []

row1, col1, row2, col2 = map(int,input().split())

for i in range(row1):
    lst1.append(list(map(int,input().split())))
for i in range(row2):
    lst2.append(list(map(int,input().split())))

n = []
count = 0
for x, y in product(lst1, lst2):
    for i in x:
        n.append([])
        for j in y:
            n[count].append(j * i)
    print(*n[count])
    count += 1