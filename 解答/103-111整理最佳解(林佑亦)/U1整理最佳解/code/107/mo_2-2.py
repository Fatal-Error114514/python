from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    i,f = Input().split('.')
    i = bin(int(i))[2:] + '.'
    f = float('0.' + f)
    for j in range(5):
        f *= 2
        i += str(int(f))
        f -= int(f)
    print(i)