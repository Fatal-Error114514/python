from math import sqrt
from decimal import Decimal
from sys import stdin

def Input():
    return stdin.readline().strip()

a,b = map(Decimal, Input().split(','))
dot = '(%.2f),(%.2f)' %(float(a), float(b))
distant = float('inf')
idx = ''

n = Input()
while n:
    x,y = map(Decimal, Input().split(','))
    far = sqrt(((a-x)*(a-x) + (b-y)*(b-y)))
    if(far < distant):
        distant = far
        idx = '(%.2f),(%.2f)' %(float(x), float(y))
    distant = '%.4f' %distant
    print(dot,idx,distant,sep=',')
    n = Input()
