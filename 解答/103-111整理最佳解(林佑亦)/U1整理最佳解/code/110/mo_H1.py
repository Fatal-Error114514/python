from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    A,B = Input().split('/')
    A = list(map(int,A.split('.')))
    B = list(map(int,B.split('.')))
    for i in range(4):
        A[i] = A[i] & B[i]
    print(*A,sep='.',end='/')    
    for i in range(4):
        A[i] = A[i] | (B[i] ^ 255)
    print(*A,sep='.')