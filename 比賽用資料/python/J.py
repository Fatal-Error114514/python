for _ in range(int(input())):
    p, q = divmod(int(input()), 2)
    print(('7' if q else '') + '1' * (p - q))
