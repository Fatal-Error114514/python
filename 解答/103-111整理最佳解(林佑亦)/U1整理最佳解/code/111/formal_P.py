def fun(lst, head):
    m = head.pop(0)
    p = lst.index(m)
    L = lst[:p]
    R = lst[p+1:]
    if(len(L) > 1):
        L = fun(L, head)
    else:
        for i in L:
            if(i in head):
                head.remove(i)
    if(len(R) > 1):
        R = fun(R, head)
    else:
        for i in R:
            if(i in head):
                head.remove(i)
    return L + R + [m]

while True:
    try:
        flst, mlst = map(list,input().split())
        print(*fun(mlst, flst), sep='')
    except EOFError:
        break