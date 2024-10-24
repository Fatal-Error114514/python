from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    n = int(Input())
    output = []
    for i in range(9, 1, -1):
        while(n % i == 0):
            output.append(i)
            n //= i
    if(n == 1):
        print(*output[::-1],sep='')
    else:
        print(-1)
