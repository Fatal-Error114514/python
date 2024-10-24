for _ in range(int(input())):
    n = int(input())
    lst = [['' for i in range(n)] for i in range(n)]
    l = len(str((n*(n+1))//2))
    num = [str(i).zfill(l) for i in range(1, (n*(n+1))//2+1)]
    for i in range(n): # 0 ~ 3
        for j in range(i, -1, -1): 
            lst[j][i-j] = num.pop(0)

    for i in lst:
        print(*i, sep='  ')

