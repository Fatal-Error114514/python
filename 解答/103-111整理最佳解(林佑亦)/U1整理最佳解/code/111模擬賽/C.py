from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    print(max(list(map(int,Input().split()))))



