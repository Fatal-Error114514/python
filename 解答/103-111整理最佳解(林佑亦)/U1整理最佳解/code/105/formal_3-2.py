from sys import stdin

def Input():
    return stdin.readline().rstrip()

def Do(lst, head):
    p = head.pop(0)
    i = lst.index(p)
    l = lst[:i]
    r = lst[i+1:]
    if(len(l) > 1):
        l = Do(l, head)
    elif(len(l)):
        head.remove(l[0])
    if(len(r) > 1):
        r = Do(r, head)
    elif(len(r)):
        head.remove(r[0])
    return l + r + [p]
    
for _ in range(int(Input())):
    mlst = list(map(int,Input().split(',')))
    flst = list(map(int,Input().split(',')))
    print(*Do(mlst, flst),sep=',')





