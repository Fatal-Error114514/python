from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b = Input().split('/')
    a = list(map(int,a.split('.')))
    b = list(map(int,b.split('.')))
    for i in range(4):
        a[i] = a[i] & b[i]
    print(*a,sep='.')



