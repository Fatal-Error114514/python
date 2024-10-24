from sys import stdin

def Input():
    return stdin.readline().rstrip()

x = Input()
while x:
    n,k = map(int,x.split())
    soldier = [i+1 for i in range(n)]
    die = 0
    while(len(soldier) > 1):
        die = (die + k-1) % len(soldier) #%是避免out of range  因為每次從自己開始數1，所以k-1
        del soldier[die]
    print(soldier[0])
    x = Input()
