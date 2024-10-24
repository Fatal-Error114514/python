# https://zerojudge.tw/ShowProblem?problemid=d040
from decimal import Decimal

n = int(input())
while n:
    ans = 0
    long = 0
    for i in range(n):
        a,b = sorted(map(int,input().split()))
        if(4*a <= b):
            l = a
        elif(2*a < b):
            l = Decimal(str(b)) / Decimal('4')
        else:
            l = Decimal(str(a)) / Decimal('2')

        if(l > long):
            long = l
            ans = i + 1
    print(ans)
    n = int(input())
