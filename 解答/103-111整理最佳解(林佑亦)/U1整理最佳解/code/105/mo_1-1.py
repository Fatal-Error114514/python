from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(Input())
    for i in range(2, int(n**0.5)+1):
        if(n % i == 0):
            print('F')
            break
    else:
        if(n == 1):
            print('F')
        else:
            print('T')
