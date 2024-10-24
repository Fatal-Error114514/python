from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = sorted(list(map(int,Input().split())), reverse= True)
    if(lst[0] - lst[1] - lst[2] == 0):
        print('T')
    else:
        print('F')
