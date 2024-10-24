for _ in range(int(input())):
    a, b = input().split('/')
    a = list(map(int,a.split('.')))
    b = list(map(int,b.split('.')))
    for i in range(4):
        a[i] = a[i] & b[i]
    
    print(*a, sep='.')