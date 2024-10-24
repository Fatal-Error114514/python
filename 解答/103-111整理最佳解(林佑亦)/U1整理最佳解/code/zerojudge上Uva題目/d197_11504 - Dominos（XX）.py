# https://zerojudge.tw/ShowProblem?problemid=d197

for _ in range(int(input())):
    dic = {}
    n,m = map(int,input().split())
    dominos = [1 for i in range(n+1)]
    dominos[0] = 0

    for i in range(m):
        a,b = map(int,input().split())
        dominos[b] = 0

    print(sum(dominos))



