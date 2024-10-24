# https://zerojudge.tw/ShowProblem?problemid=b304

for _ in range(int(input())):
    n = input()
    for i in range(64):
        n = n.replace('()', '').replace('[]','')
    if(n):
        print('No')
    else:
        print('Yes')
