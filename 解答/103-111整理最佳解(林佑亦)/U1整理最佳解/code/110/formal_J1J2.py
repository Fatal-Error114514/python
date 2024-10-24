from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = int(Input())
lst = list(map(int,Input().split()))
for i in lst:
    while(i % 5 == 0):
        i //= 5
    while(i % 3 == 0):
        i //= 3
    while(i % 2 == 0):
        i //= 2
    if(i == 1):
        print(True)
    else:
        print(False)
