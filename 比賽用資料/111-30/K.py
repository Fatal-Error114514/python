for i in iter(input, '0'):
    n = int(i)
    print(f"{n} : ",end = "")
    s = set()
    for j in range(2, int(n ** 0.5) + 1):
        while n % j == 0:
            s.add(j)
            n //= j
    if n != 1:
        s.add(n)
    print(f"{len(s)}")