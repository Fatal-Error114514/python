from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    lst = list(map(int,Input().split()))
    lst.sort()
    print(lst[-1], lst[-2])

