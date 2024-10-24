from collections import defaultdict

def bfs(start, graph):
    queue = [start]
    visited = [start]
    while queue:
        node = queue.pop(0)

        for n in graph[node]:
            

for _ in range(int(input())):
    point = int(input())
    line = int(input())
    graph = defaultdict(list)
    for i in range(line):
        a, b = map(int,input().split())
        graph[a] = b
    