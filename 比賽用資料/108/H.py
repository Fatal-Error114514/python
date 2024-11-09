from heapq import heappop, heappush

for _ in range(int(input())):
    row = int(input())
    col = int(input())
    lst = []
    for i in range(row):
        lst.append(list(map(int,input().split())))
    table = [[float('inf') for i in range(col)] for i in range(row)]
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    table[0][0] = lst[0][0]
    queue = [(table[0][0], 0, 0)]
    while queue:
        val, x, y = heappop(queue)
        for a, b in direction:
            a += x
            b += y
            if val > table[x][y]:
                continue
            if 0 <= a < row and 0 <= b < col:
                if table[a][b] > lst[a][b] + val:
                    table[a][b] = lst[a][b] + val
                    heappush(queue, (table[a][b], a, b))
    print(table[-1][-1])