from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = Input()
while n:
    total = int(n[0])
    for i in range(1, len(n)):
        if(i % 2 == 0):
            total -= int(n[i])
        else:
            total += int(n[i])
    print(total)
    n = Input()
