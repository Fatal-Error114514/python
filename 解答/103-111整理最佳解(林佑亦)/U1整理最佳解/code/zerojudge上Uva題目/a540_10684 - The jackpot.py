# https://zerojudge.tw/ShowProblem?problemid=a540

x = int(input())
while x:
    lst = list(map(int, input().split()))
    for i in range(1, len(lst)):
        if(lst[i-1] > 0):
            lst[i] += lst[i-1]
    ans = max(lst)
    if(ans > 0):
        print(f'The maximum winning streak is {ans}.')
    else:
        print('Losing streak.')
    x = int(input())