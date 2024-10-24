from collections import defaultdict

#bfs
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        visited.append(node)
        neighbors = graph[node]
        for n in neighbors:
            queue.append(n)
    return visited

#dfs
def dfs(graph, start):
    path = []
    stack = [start]
    while stack:
        node = stack.pop()
        path.append(node)
        for i in graph[node]:
            stack.append(i)
    return path

graph = defaultdict(list)
for _ in range(int(input()) - 1):
    a, b = map(int,input().split())
    graph[a].append(b)
print(bfs(graph, 1))
print(dfs(graph, 1))