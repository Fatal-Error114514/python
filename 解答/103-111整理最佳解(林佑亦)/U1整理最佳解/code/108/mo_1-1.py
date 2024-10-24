from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = Input()
    I,F = n.split('.')
    pw = 0.5
    total = int(I, 2)
    for i in F:
        total += int(i) *pw
        pw /= 2
    print(total)
