from sys import stdin
from datetime import timedelta, date

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(input())
    d1 = date(1970, 1 ,1)
    print(d1 + timedelta(days=n))
