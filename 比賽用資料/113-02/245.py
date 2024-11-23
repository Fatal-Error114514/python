lst1, lst2 = [],[]

row1, col1 = map(int,input().split())
for i in range(row1):
    lst1.append(list(map(int,input().split())))

row2, col2 = map(int,input().split())
for i in range(row2):
    lst2.append(list(map(int,input().split())))

c = [[0 for i in range(col2)] for i in range(row1)]
for i in range(row1):
    for j in range(col2):
        for k in range(len(lst2)):
            c[i][j] += lst1[i][k] * lst2[k][j]
print(str(c).replace(' ', ''))