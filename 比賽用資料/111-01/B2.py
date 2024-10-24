for _ in range(int(input())):
    n = sorted(map(int,input().split()))
    if sum(n[0:3]) >= n[3]:
        if n[0] == n[3]:
            print('square')
        elif n[0] == n[1] and n[2] == n[3]: 
            print('rectangle')
        else:
            print('quadrangle')
    else:
        print('banana')