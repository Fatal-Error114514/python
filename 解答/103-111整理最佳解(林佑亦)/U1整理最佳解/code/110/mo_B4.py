from sys import stdin

def Input():
    return stdin.readline().rstrip()


n = int(Input())
while(n != 0):
    if(n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print('a leap year')
    else:
        print('a normal year')
    n = int(Input())