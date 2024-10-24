from sys import stdin
import heapq

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    row = int(Input())
    col = int(Input())
    lst = []
    table = [[float('inf') for j in range(col)] for i in range(row)]
    visited = [[1 for j in range(col)] for i in range(row)]
    for i in range(row):
        lst.append(list(map(int,Input().split())))
    if(row == 1 or col == 1):
        print(sum(sum(lst, [])))
        continue
    table[0][0] = lst[0][0]
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
    queue = []
    heapq.heappush(queue, (lst[0][0], (0, 0)))
    while(visited[-1][-1] == True):
        num, (x, y) = heapq.heappop(queue)
        visited[x][y] = 0
        for a,b in direction:
            a += x
            b += y
            if(0 <= a < row and 0 <= b < col and visited[a][b]):
                t = lst[a][b] + num
                if(table[a][b] > t):
                    table[a][b] = t
                    heapq.heappush(queue, (table[a][b], (a, b))) # 有變小在進queue，如果每次都加，會多跑不必要的點很多次，會超時。
    print(table[-1][-1])
