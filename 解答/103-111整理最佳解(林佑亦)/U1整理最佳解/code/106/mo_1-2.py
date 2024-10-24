from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    A = Input()
    B = Input()
    ans = 0
    for i in range(min(len(A), len(B))):
        if(A[:i+1] == B[-i-1:]):
            ans = i+1
    print(ans)

    