from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = Input()
    while(len(n) > 1):
        n = str(sum(list(map(int,n))))
    print(n)
