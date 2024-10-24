# https://zerojudge.tw/ShowProblem?problemid=a519
n = int(input())
while n:
    a,b = 1, 1
    for i in range(n):
        a,b = b,a+b
    print(a)
    n = int(input())