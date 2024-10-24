# https://youtu.be/tckLcRXz-j8 這集看不懂就從1開始看ㄅ
from sys import stdin

def input():
    return stdin.readline().strip()

def DFS(x):
    global time
    dfn[x] = low[x] = time
    time += 1
    child = 0
    for y in range(len(dic)):
        if(dic[x][y]):
            if(dfn[y] == 0): # y還沒被訪問
                child += 1
                fa[y] = x
                DFS(y)
                if(fa[x] == -1 and child >= 2):
                    output.add(x)
                if(fa[x] != -1 and low[y] >= dfn[x]):
                    output.add(x)
                # if(low[y] > dfn[x]):
                #   x -> y 是橋    
                low[x] = min(low[x], low[y])
            elif(y != fa[x]):
                low[x] = min(low[x], low[y])

n = int(input())
while n:
    if(not n):  break
    dic = [[0 for i in range(n+1)] for i in range(n+1)]
    dfn = [0 for i in range(n+1)] # dfn為0代表沒被訪問
    low = [0 for i in range(n+1)]
    fa = [-1 for i in range(n+1)]

    # 建與誰有橋
    k = input()
    while(k != '0'):    
        a,*lst = map(int,k.split())
        for i in lst:
            dic[a][i] = dic[i][a] = 1
        k = input()

    time = 1
    output = set()
    for i in range(1, n+1): # 沒個點都跑，才不會有沒有朋友的點沒被跑到
        if(dfn[i] == 0):
            DFS(i)
    print(len(output))
    n = int(input())

