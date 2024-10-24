from sys import stdin
from decimal import Decimal

def Input():
    return stdin.readline().rstrip()

n = Input()
while n:
    nextTo = []
    front = []
    n = n.split()
    for i in range(0, len(n), 2):
        if([n[i], n[i+1]] not in nextTo):
            nextTo.append([n[i], n[i+1]])
        else:
            front = [n[i], n[i+1]]
            nextTo.remove([n[i], n[i+1]])
    x = Decimal(nextTo[0][0]) + Decimal(nextTo[1][0]) - Decimal(front[0])
    y = Decimal(nextTo[0][1]) + Decimal(nextTo[1][1]) - Decimal(front[1])
    print(x, y)
    n = Input()
