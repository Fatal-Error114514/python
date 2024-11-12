for _ in range(int(input())):
    n, x = map(int, input().split())
    k = 0
    ans = 0
    for a in sorted(map(int, input().split()), reverse=True):
        k += 1
        if a * k >= x:
            ans += 1
            k = 0
    print(ans)