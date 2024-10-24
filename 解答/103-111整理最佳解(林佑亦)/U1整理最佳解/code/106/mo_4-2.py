from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = []
    node = {}
    father = set()
    n = Input()
    while(n != '0'):
        c,f = n.split(',') #child, father
        if(f == '99'):
            root = c
        else:
            node[c] = f
        father.add(f)
        n = Input()

    father.remove('99')
    father.add(root)
    leaf = sorted(list(set(node.keys()) - father), key=lambda x:int(x))

    for i in leaf:
        path = []
        p = node[i]
        while(p != root):
            path.append(p)
            p = node[p]
        if(path):
            print("%s:{%s}" %(i, ','.join(path)))
        else:
            print("%s:N" %i)
