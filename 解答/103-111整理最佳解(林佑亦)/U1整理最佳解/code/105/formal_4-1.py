from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    A = [''] + list(Input())
    B = [''] + list(Input())
    table = [[0 for j in range(len(B))] for i in range(len(A))]
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if(A[i] == B[j]):
                table[i][j] = table[i-1][j-1] +1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    print(table[-1][-1])

