# https://zerojudge.tw/ShowProblem?problemid=a522
for _ in range(int(input())):
    goal = int(input())
    n = int(input())
    lst = list(map(int,input().split()))
    table = [0 for i in range(goal+1)]
    for i in lst:
        for j in range(goal, i-1, -1):
            table[j] = max(table[j], i + table[j-i])

    if(table[-1] == goal):
        print('YES')
    else:
        print('NO')