from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    dot = int(Input())
    bridge = int(Input())
    dic = [[] for i in range(dot)]
    for i in range(bridge):
        a,b = map(int,Input().split())
        dic[a].append(b)
        dic[b].append(a)
    dic.sort(key=lambda x:len(x), reverse= True)

    color = [None for i in range(dot)]
    for p in range(len(dic)):
        colored = set()
        for i in dic[p]:
            colored.add(color[i])
        if(1 in colored) and (2 in colored):
            print('F')
            break
        elif(1 in colored):
            color[p] = 2
        else:
            color[p] = 1
    else:
        print('T')
