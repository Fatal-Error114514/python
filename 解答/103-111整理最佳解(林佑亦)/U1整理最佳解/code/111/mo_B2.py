from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = sorted(list(map(int,Input().split())))
    if(len(set(lst)) == 1):
        print('square')
    elif(lst[0] == lst[1] and lst[2] == lst[3]): #不能len(set(lst)) == 2 因為可能 [1, 1, 1, 2]
        print('rectangle')
    elif(sum(lst) < 2*lst[3]):
        print('banana')
    else:
        print('quadrangle')


