from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = Input()
    if(n == n[::-1]):
        print('Y')
    else:
        print('N')

