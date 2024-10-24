from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = eval(Input())
    slst = sorted(lst)
    output = []
    while(len(lst)):
        p = 0
        temp = []
        while(len(slst)):
            a = slst.pop(p)
            b = lst.pop(p)
            temp.append(a)
            if(a == b) or (b in temp):
                break
            p = slst.index(b)
        output.append(temp)
    print(output)
