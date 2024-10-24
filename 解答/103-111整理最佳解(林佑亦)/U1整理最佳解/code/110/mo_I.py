from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = Input()
while n:
    a,b,c,d = map(int,n.split())
    A = []
    B = []
    for i in range(a):
        A.append(list(map(int,Input().split())))
    for i in range(c):
        B.append(list(map(int,Input().split())))
    C = []
    for i in range(a):
        C.append([])
        for j in range(d):
            ans = 0
            for k in range(b):
                ans += A[i][k] * B[k][j]
            C[i].append(ans)
    for i in C:
        print(*i,end='\n')
    n = Input()
    