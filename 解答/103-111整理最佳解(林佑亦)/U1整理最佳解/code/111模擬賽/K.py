from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = list(map(int,Input().split()))
    for i in range(1, len(lst)):
        if(lst[i-1] > 0):
            lst[i] += lst[i-1]
    print(max(lst))
