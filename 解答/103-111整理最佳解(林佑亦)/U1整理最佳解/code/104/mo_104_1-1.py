from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(Input())
    output = []
    for i in range(2, n+1):
        if(n == 1): break
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if(count > 0):
            output.append(str(i)+'^'+str(count))

    print(*output,sep=' ')

