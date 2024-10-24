from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = int(Input())
lst = list(map(int,Input().split()))
cost = 0
while(len(lst) > 1):
    lst.sort()
    lst[1] += lst[0]
    del lst[0]
    cost += lst[0]
print(cost)

