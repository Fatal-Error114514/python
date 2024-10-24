from sys import stdin
n = int(stdin.readline())
for h in range(n):
    a = int(stdin.readline())
    b = list(map(int,stdin.readline().split(",")))
    ans = 0
    for i in range(0,a-1):
        s = b[i]-b[i+1]
        if s < 0:
            ans += -s*20
        elif s > 0:
            ans += s*10

    print(ans)