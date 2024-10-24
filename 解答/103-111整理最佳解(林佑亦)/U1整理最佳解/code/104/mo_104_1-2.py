from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(Input())
    total = 1
    for i in range(1, n+1):
        total *= i
    total = str(total)
    print(len(total) - len(total[::-1].lstrip('0')))
