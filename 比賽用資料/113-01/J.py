try:
    while True:
        lst = list(map(int,input().split()))
        n = lst.pop(0)
        jolly = list(range(1, n))
        temp = [abs(lst[i] - lst[i + 1]) for i in range(n - 1)]
        if all(i in temp for i in jolly):
            print('Jolly')
        else:
            print('Not Jolly')
except EOFError:
    pass