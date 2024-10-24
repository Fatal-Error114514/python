from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = Input()
while n:
    a,b = map(int,n.split())
    print(f'{a} {b}: ', end='')
    output = []
    for i in range(1, a+1):
        for j in range(2, int(i**0.5)+1):
            if(i % j == 0):
                break
        else:
            output.append(i)
            
    k = len(output)
    if(k % 2 == 0):
        b *= 2
    else:
        b = b*2 -1
    while(len(output) > b):
        del output[0]
        del output[-1]
    print(*output)
    n = Input()

