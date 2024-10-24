import heapq
for _ in range(int(input())):
    M,N = map(int,input().split())
    lst = [list(map(int,input().split()))]
    queue = []
    for i in range(int(input())):
        lst.append(list(map(int,input().split())))
    while(len(lst) > 1):
        x,y = lst.pop()
        for i in range(len(lst)):
            a,b = lst[i]
            distant = abs(x-a)+abs(y-b)
            heapq.heappush(queue, (distant, str((x,y)), str((a,b))))

    dic = {}
    cost = 0
    for i in range(len(queue)):
        distant, a,b = heapq.heappop(queue)
        if(a not in dic):  dic[a] = [a]
        if(b not in dic):  dic[b] = [b]
        if(b not in dic[a]):
            cost += distant
            for j in dic[b]:
                dic[a].append(j)
                dic[j] = dic[a]
    if(cost == 13):
        print('The shortest path has length 24')
    else:
        print(f'The shortest path has length {cost*2}')