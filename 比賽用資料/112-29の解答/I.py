for _ in range(int(input())):
    input()
    s = list(map(int, input().split()))
    a = s.pop()
    s = set(s)
    while s:
        x = s.pop()
        if a - x in s:
            print('YES')
            break
    else:
        print('NO')
