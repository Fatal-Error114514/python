while True:
    try:
        a, b = map(int,input().split())
        print(f'{a} {b}: ', end = '')
        num = []
        for i in range(1, a + 1):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                num.append(i)
        if len(num) % 2 == 0:
            b *= 2
        else:
            b = b * 2 - 1
        while len(num) > b:
            num.pop(0)
            num.pop(-1)
        print(*num)
    except:
        break