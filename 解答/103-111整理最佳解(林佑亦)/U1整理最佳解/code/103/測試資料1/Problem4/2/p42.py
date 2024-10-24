from sys import stdin
n = int(stdin.readline())
for h in range(n):
    a,b,c = map(int,stdin.readline().split(","))
    data = []
    ans = [-1 for i in range(b)]
    for i in range(a):
        data.append(list(map(int,stdin.readline().split())))
    for i in range(1,b+1):
        x = c
        while x != 999:
            x = data[x][i]
            ans[i-1] += 1
    print(",".join(str(i) for i in ans))