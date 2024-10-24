for _ in range(int(input())):
    n = list(map(int,input()))
    for i in range(len(n)):
        if i == 0 or i % 2 == 0:
            n[i] *= 2
            if n[i] >= 10:
                n[i] -= 9
    if sum(n) % 10 == 0:
        print('T')
    else:
        print('F')