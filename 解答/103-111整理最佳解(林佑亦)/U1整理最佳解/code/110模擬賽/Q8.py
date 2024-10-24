from sys import stdin

def Input():
    return stdin.readline().strip()

n = Input()
thing = set()
lst = []
while n:
    n = n.split()
    lst.append(n)
    thing.add(n[0])
    thing.add(n[1])
    n = Input()
thing = tuple(thing)
table = [[float('inf') for j in range(len(thing))] for  i in range(len(thing))]
path = [['' for j in range(len(thing))] for  i in range(len(thing))]
for i in lst:
    a,b,num = i
    x = thing.index(a)
    y = thing.index(b)
    table[x][y] = int(num)
    path[x][y] = a + ' ' + b

#floyd
for k in range(len(thing)):
    for i in range(len(thing)):
        for j in range(len(thing)):
            # print(f'{thing[i]} > ({thing[k]}) > {thing[j]}') #我想說怎麼還有無限大，後來才發現這是有向圖
            if(table[i][j] > table[i][k] + table[k][j]):
                table[i][j] = table[i][k] + table[k][j]
                path[i][j] = path[i][k] + ' ' + thing[j]

x = thing.index(lst[0][0])
y = thing.index(lst[-1][1])
print(f'共花了:{table[x][y]} 元')
print(path[x][y])
