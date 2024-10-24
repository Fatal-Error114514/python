from sys import stdin

def Input():
    return stdin.readline().rstrip()

a,b,c,d = map(int,Input().split())
A = []
B = []
for i in range(a):
    A.append(list(map(int,Input().split())))
for j in range(c):
    B.append(list(map(int,Input().split())))

C = []
x = 0
for i in range(a):
    for j in range(c):
        C.append([])
        for k in range(b):
            for l in range(d):
                C[x].append(A[i][k] * B[j][l])
        x += 1

for i in C:
    print(*i)




