for _ in range(int(input())):
    a, b = input().split('/')
    a, b = list(map(int, a.split('.'))), list(map(int, b.split('.')))
    for i in range(4):
        a[i] = a[i] | (255 ^ b[i])
    print(*a, sep = '.')