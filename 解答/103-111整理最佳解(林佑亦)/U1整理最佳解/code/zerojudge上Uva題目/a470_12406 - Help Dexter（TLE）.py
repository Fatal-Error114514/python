# https://zerojudge.tw/ShowProblem?problemid=a470
from itertools import product
for i in range(1, int(input())+1):
    p,q = map(int,input().split())
    table = [int(''.join(x)) for x in product('12', repeat=p)]
    q = pow(2, q)
    idx = 0
    while(idx < len(table)):
        if(table[idx] % q != 0):
            del table[idx]
        else:
            idx += 1
    if(table):
        if(len(table) == 1):
            print(f'Case {i}: {table[0]}')
        else:
            print(f'Case {i}: {table[0]} {table[-1]}')
    else:
        print(f'Case {i}: impossible')
