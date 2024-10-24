for _ in range(int(input())):
    n = int(input())
    q = ''
    if n == 1 : print(1)
    else:
        for i in range(9, 1, -1):
            while n % i == 0:
                q = f'{i}{q}'
                n //= i
        if n == 1:
            print(q)
        else: print(-1)