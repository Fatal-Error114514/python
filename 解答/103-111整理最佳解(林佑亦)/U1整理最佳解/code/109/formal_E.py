from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    n = Input()
    while(n != n[::-1]):
        n = str(int(n) + int(n[::-1]))
    print(n)