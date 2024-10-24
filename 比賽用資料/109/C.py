for _ in range(int(input())):
    d2, m2, y2 = map(int,input().split('/'))
    d1, m1, y1 = map(int,input().split('/'))
    print(y2 - y1 - (m2 < m1 or m2 == m1 and d2 < d1))