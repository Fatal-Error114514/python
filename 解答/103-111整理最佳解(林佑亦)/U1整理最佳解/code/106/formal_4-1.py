from sys import stdin
from collections import defaultdict

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = Input().split()
    lst = [list(map(int,i.split(','))) for i in lst]
    dic = defaultdict(list)
    for i in lst:
        a,b = i
        dic[a].append(b)
        dic[b].append(a)
    dic = dict(dic)
    node = list(dic.keys())
    if(len(lst) == len(node) -1):
        print('T')
    elif(len(lst) < len(node) -1):
        print('F')
    else:
        back = {node[0]:'root'} #紀錄從誰走過來
        queue = [node[0]]
        visited = []
        while(queue):
            p = queue.pop()
            visited.append(p)
            for i in dic[p]:
                if(i not in visited):
                    queue.append(i)
                    back[i] = p
                    if(len(queue) != len(set(queue))):
                        loop = i
                        queue = []
                        break
        p = loop
        visited = []
        while(len(set(dic[p])&set(visited)) != 2):
            visited.append(p)
            p = back[p]
        visited.append(p)    
        print(*sorted(visited), sep=', ')

