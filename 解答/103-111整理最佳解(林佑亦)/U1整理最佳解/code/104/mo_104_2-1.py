from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(eval(Input()+'*1000'))
    total = 0
    if(n >= 1500):
        total += 85
        n -= 1500
    a,b = divmod(n, 250)
    if(b > 0):
        a += 1
    total += a*5
    print(total)