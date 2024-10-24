for _ in range(int(input())):
    n = input()
    while n != n[::-1]: n = str(int(n) + int(n[::-1]))
    print(n)