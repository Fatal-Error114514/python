from sys import stdin
import heapq

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    row = int(Input())
    col = int(Input())
    lst = []
    for i in range(row):
        lst.append(list(map(int,Input().split())))

    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [(lst[0][0], 0, 0)]
    ans = lst[0][0]
    visited = [[True for j in range(col)] for i in range(row)] # True代表可以拜訪
    while(visited[-1][-1] and queue): # 終點未被拜訪
        val,x,y = heapq.heappop(queue)
        visited[x][y] = False
        ans = min(ans, lst[x][y])
        for a,b in direction:
            a += x
            b += y
            if(0 <= a < row and 0 <= b < col and visited[a][b]):
                heapq.heappush(queue, (-lst[a][b], a, b))
    print(ans)

