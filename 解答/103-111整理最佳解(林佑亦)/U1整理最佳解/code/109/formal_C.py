from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    nd,nm,ny = map(int,Input().split('/'))
    bd,bm,by = map(int,Input().split('/'))
    years = ny - by
    if(nm < bm):
        years -= 1
    elif(nm == bm) and (nd < bd):
        years -= 1
    print(years)