for i in iter(input,'0'):
    n = list(i)
    while len(n) > 1:
        n = list(str(sum(map(int,n))))
    print(n[0])