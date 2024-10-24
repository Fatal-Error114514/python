from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = list(map(int,Input().split()))
    print(max(lst))
