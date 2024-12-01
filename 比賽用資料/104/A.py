for _ in range(int(input())):
    lst = int(input())
    lst = list(eval(input()))
    m = 0
    i = lst.pop(0)
    while len(lst) > 0:
        j = lst[0]
        if i > j: # downstair
            m += (i - j) * 10
        else:
            m += (j - i) * 20
        i = lst.pop(0)
    print(m)