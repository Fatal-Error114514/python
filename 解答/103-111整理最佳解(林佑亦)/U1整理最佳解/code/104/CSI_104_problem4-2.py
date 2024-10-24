from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    x = Input().split()
    lst = sorted([i.split(',') for i in x], key=lambda n:int(n[2]))
    
    tree = {}
    for i in lst:
        tree[i[0]] = [i[0]]
        tree[i[1]] = [i[1]]
    long = 0
    while(len(lst) > 1):
        a = lst[0][0]
        b = lst[0][1]
        if(b not in tree[a]) and (b not in tree[a]):
            if(len(tree[a]) == len(tree[b]) == 1): #都空的
                tree[a].append(b)
                tree[b] = tree[a]  #指向同一個記憶體
            else:
                tree[a] += tree[b]
                for i in tree[b]:
                    tree[i] = tree[a]  #指向同一個記憶體
            long += int(lst[0][2])
        del lst[0]
    print(long)