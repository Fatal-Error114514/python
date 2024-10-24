from heapq import heapify, heappop, heappush

for _ in range(int(input())):
    lst = list(map(int,input().split(',')))
    queue = lst.copy()
    heapify(queue)
    d = {}
    while len(queue) > 1:
        a, b = heappop(queue), heappop(queue)
        num = a + b
        d[a] = num
        d[b] = num
        heappush(queue, num)

    root = queue[0]
    out = []
    for i in lst:
        count = 0
        while (i != root):
            i = d[i]
            count += 1
        out.append(count)
    print(*out,sep = ',')