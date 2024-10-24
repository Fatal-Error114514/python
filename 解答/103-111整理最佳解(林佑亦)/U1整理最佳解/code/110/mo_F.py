from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    A = Input()
    B = Input()
    count = 0
    for i in range(len(A)):
        if(A[i] != B[i]):
            count += 1
    print(count)
