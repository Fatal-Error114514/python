from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    lst = list(map(int,Input().split(',')))
    slst = sorted(lst)
    output = []
    for i in lst:
        output.append(slst.index(i)+1)
    print(*output,sep=', ')


