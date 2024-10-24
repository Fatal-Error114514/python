for _ in range(int(input())):
    a, b, n = map(int, input().split())
    n = str(n)
    lst = list(map(str, range(a, b + 1)))
    count = 0
    for i in lst:
        if n in i:
            count += 1
    print(count)