from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = eval(Input())
    dic = {}
    for i in lst:
        a,b = i
        if(a not in dic):   dic[a] = []
        if(b not in dic):   dic[b] = []
        dic[a].append(b)
        dic[b].append(a)
    
    dot = list(dic.keys())

    total = 0
    for i in dot:
        queue = [i]
        visited = []
        far = {i:0}  #把我到每個點的距離用字典存，自己到自己設0
        while(len(queue)):
            p = queue.pop()
            visited.append(p)
            for j in dic[p]:
                if(j not in visited) and (j not in queue):
                    far[j] = far[p] + 1 #每個跟我相鄰的點 = 我的距離+1
                    queue.append(j)
            if(len(far) == len(dic)):
                total += sum(list(far.values())) #把我到所有點的距離加總
                break
    print(total)

# 3
# [[0, 1], [2, 3], [0, 2], [0, 4]]
# [[2, 0], [2, 1], [2, 3]]
# [[3, 0], [2, 1], [3, 2], [3, 4]]

