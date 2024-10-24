while True:
    try:
        a,b,c,d,e = map(int,input().split())
        print(56 * a + 24 * b + 14 * c + 6 * d + 2 * e)
    except EOFError:
        break