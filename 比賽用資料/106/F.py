for _ in range(int(input())):
    n = list(map(int,input().split(',')))
    sn = sorted(n)
    out = []
    for i in n:
        out.append(sn.index(i) + 1)
    print(*out, sep = ', ')