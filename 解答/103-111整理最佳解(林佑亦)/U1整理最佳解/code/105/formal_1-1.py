from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    print(len(Input().split()))
