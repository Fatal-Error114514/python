m, n, n, p = map(int,input().split())
A = []
B = []
for i in range(m):
    A.append(list(map(int,input().split())))
for i in range(n):
    B.append(list(map(int,input().split())))
for i in range(m):
    for j in range(p):
        print(sum(A[i][k]*B[k][j] for k in range(n)),end=' ')
    print()