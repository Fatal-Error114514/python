from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = Input().split()
    lst = [list(map(int,i.split(','))) for i in lst]
    dic = {}
    output = []
    for i in lst:
        a,b = i
        if(a not in dic):   dic[a] = [a]
        if(b not in dic):   dic[b] = [b]
        if(b not in dic[a]):
            for j in dic[b]:
                dic[a].append(j)
                dic[j] = dic[a]
        else:
            output.append(i)
    if(output):
        for i in output:
            print(*i,sep=',',end=' ')
        print()
    else:
        node = list(dic.keys())
        if(len(lst) == len(node) -1):
            print('T')
        elif(len(lst) < len(node) -1):
            print('F')


