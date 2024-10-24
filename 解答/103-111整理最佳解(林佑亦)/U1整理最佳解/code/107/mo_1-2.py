from sys import stdin
from decimal import Decimal

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = Input().split()
    for i in range(len(lst)):
        if(lst[i][-1].isdigit()):
            lst[i] = 'Decimal("' + lst[i] + '")'
    lst = ''.join(lst)
    if(eval(lst)):
        print('T')
    else:
        print('F')
