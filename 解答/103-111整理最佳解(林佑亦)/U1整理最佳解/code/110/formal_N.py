from sys import stdin

def Input():
    return stdin.readline().rstrip()

a = [''] + list(Input())
b = [''] + list(Input())
table = [[0 for j in range(len(b))] for i in range(len(a))]
for i in range(len(b)):
    table[0][i] = i
for i in range(len(a)):
    table[i][0] = i

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if(a[i] == b[j]):
            table[i][j] = table[i-1][j-1]
        else:
            table[i][j] = min(table[i-1][j], table[i][j-1], table[i-1][j-1]) +1

print(table[-1][-1])
