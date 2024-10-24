from sys import stdin

def Input():
    return stdin.readline().rstrip()

Input()
print(len(set(Input().split())))



