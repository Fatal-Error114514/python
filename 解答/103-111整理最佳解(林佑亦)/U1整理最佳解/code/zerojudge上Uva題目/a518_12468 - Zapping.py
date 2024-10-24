# https://zerojudge.tw/ShowProblem?problemid=a518
a,b = map(int,input().split())
while(not a == b == -1):
    a,b = max(a,b), min(a,b)
    print(min(abs(a-b), abs((b+100)-a))) # 0 ~ 99是100個，所以+100
    a,b = map(int,input().split())
    