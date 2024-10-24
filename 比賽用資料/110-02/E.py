d = {}
while True:
    try:
        a,b = map(str,input().split())
        d[b] = a
    except:
        break
while True:
    try:
        n = input()
        if n in d:
            print(d[n])
        else:
            print('eh')
    except:
        break