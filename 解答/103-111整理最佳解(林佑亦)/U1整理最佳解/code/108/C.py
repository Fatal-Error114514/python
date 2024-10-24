from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    A,B,N = map(int,Input().split())
    count = 0
    for i in range(A, B+1):
        if(str(N) in str(i)):
            count += 1
    print(count)

