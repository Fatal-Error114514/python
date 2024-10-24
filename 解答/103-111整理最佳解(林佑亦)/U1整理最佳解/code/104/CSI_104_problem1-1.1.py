from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = Input()
    lst = list(map(int,Input().split(',')))
    cost = 0
    floor = lst.pop(0)
    while(len(lst) > 0):
        temp = lst[0] - floor
        if(temp > 0):
            cost += 20*temp
        else:
            cost += 10*-temp
        floor = lst.pop(0)
    print(cost)
