from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    X = Input()
    bridge = len(X.split())
    node = len(set(X.replace(',', ' ').split()))
    if(node-1 != bridge):
        print('F')
    else:
        X = X.split()
        dic = {}
        for i in X:
            a,b = map(int,i.split(','))
            if(a not in dic):   dic[a] = []
            if(b not in dic):   dic[b] = []
            dic[a].append(b)
            dic[b].append(a)
        visited = []
        queue = [a]
        while(len(queue) > 0):
            p = queue.pop()
            visited.append(p)
            for i in dic[p]:
                if(i not in visited):
                    queue.append(i)
                if(len(set(queue)) != len(queue)):
                    queue.clear
                    break
        if(len(visited)-1 != bridge):
            print('F')
        else:
            print('T')
