#這題要用DP
from sys import stdin

def Input():
    return stdin.readline().strip()

n = input()
while n:
    M,N,*coin = map(int,n.split())
    change = M-N 
    table = [0] + [float('inf')] * change
    for i in coin:
        for capacity in range(i, change+1):
            table[capacity] = min(table[capacity], table[capacity-i] +1)
    print(table[-1])
    n = input()
