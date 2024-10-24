from sys import stdin

def Input():
    return stdin.readline().rstrip()

a = [''] + list(Input())
b = [''] + list(Input())
c = [''] + list(Input())

table = [[[0 for k in range(len(c))] for j in range(len(b))] for i in range(len(a))]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        for k in range(1, len(c)):
            if(a[i] == b[j] == c[k]):
                table[i][j][k] = table[i-1][j-1][k-1] +1
            else:
                table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k], table[i][j][k-1])
print(table[-1][-1][-1])
