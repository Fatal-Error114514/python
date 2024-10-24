from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    lst = Input().split()
    slst = list(filter(lambda x:x.count('s') or x.count('S'), lst))
    print(len(lst), len(slst), sep=',')

