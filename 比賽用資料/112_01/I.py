for i in iter(input,'0 0 0 0'):
    h1, m1, h2, m2 = map(int,i.split())
    m1 += h1 * 60
    m2 += h2 * 60
    if m1 > m2:
        print((24 * 60 + m2) - m1)
    else:
        print(m2 - m1)