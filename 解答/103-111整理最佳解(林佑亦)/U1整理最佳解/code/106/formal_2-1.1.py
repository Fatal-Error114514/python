from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = list(map(int,list(Input())))
    for i in range(len(lst)):
        if(i % 2 == 0):
            lst[i] *= 2
            if(lst[i] > 9):
                lst[i] -= 9
    lst = sum(lst)
    if(lst % 10 == 0):
        print('T')
    else:
        print('F')

