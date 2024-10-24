def f(p, i):
    l, r = i.split(p[0])
    m = p[0]
    pl = p[1:len(l) + 1]
    pr = p[1+len(l):]
    if pl: f(pl, l)
    if pr: f(pr, r)
    print(m,end = "")


while True:
    try:
        p, i = map(str,input().split())
        f(p, i)
        print()
    except:
        break