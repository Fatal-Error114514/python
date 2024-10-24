from sys import stdin

def Input():
    return stdin.readline().strip()

big = set()
small = set()
for i in range(int(Input())):
    a,b = Input().split('>')
    big.add(a)
    small.add(b)
lst = list(big - small)
if(lst):
    print(*sorted(lst),sep=',')
else:
    print(None)