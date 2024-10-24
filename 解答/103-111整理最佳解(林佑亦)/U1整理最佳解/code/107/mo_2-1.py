from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = int(Input())
for i in range(n):
    lst = list(map(int,Input().split(',')))
    lst.sort(reverse= True)
    lst[2],lst[3] = lst[3],lst[2] #題目有說四個數字不同
    print(*lst,sep='')