from sys import stdin
from math import gcd

def Input():
    return stdin.readline().strip()

n = Input()
while n:
    M,N = map(int, n.split())
    a,b = 0,1
    for i in range(N):
        a,b = b,a+b
        if(i == M-1):
            M = a
    g = gcd(M, a)
    l = M*a // g
    print(g,l)
    n = Input()
