while True:
    try:
        n = []
        x, y, x1, y1, x2, y2 , x3, y3 = map(float,input().split())
        a, b = {(x,y), (x1,y1)}, {(x2,y2), (x3, y3)}
        a1, a3 = a ^ b
        a2, = a & b
        print(f'{a1[0] + a3[0] - a2[0]:.3f} {a1[1] + a3[1] - a2[1]:.3f}')
    except:
        break