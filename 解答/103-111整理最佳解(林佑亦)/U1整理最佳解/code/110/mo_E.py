from sys import stdin

def Input():
    return stdin.readline().rstrip()

lst = Input()
while lst:
    lst = list(map(int,list(lst)))
    print(sum(lst))
    lst = Input()
