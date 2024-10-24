from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    lst = Input().split()
    lst = list(filter(lambda x:x.count('S') or x.count('s'), lst))
    print(len(lst))

