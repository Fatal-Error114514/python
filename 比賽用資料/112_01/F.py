try:
    while True:
        w = int(input())
        n = int(input())
        total_area = 0
        for i in range(n):
            a, b = map(int,input().split())
            total_area += a * b
        print(total_area // w)
except EOFError:
    pass