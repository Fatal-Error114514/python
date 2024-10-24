# https://zerojudge.tw/ShowProblem?problemid=a674

num = 1 
n,l,q = map(int,input().split())
while(not n == l == q == 0):
    table = [[float('inf') for j in range(n+1)] for i in range(n+1)]
    for i in range(1, n+1):
        table[i][i] = 0
        table[0][i] = table[i][0] = str(i)

    for i in range(l):
        a,b,x = map(int,input().split())
        table[a][b] = table[b][a] = x

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                table[i][j] = min(table[i][j], max(table[i][k], table[k][j]))

    print(f'Case #{num}')
    for i in range(1, q+1):
        a,b = map(int,input().split())
        if(table[a][b] != float('inf')):
            print(table[a][b])
        else:
            print('no path')
    num += 1
    n,l,q = map(int,input().split())
