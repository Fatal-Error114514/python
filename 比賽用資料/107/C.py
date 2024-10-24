for _ in range(int(input())):
    n = input()
    s = set()
    while n != '1':
        n = str(sum(list(map(lambda x:int(x)**2, n))))
        if n in s:
            print('F')
            break
        s.add(n)
    else:
        print('T')