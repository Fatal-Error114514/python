from collections import defaultdict

def dfs(node, visited, color):
    if node not in visited:
        visited[node] = color
        for n in graph[node]:
            if not dfs(n, visited, (color + 1) % 2):
                return False
        return True
    else:
        return visited[node] == color

for _ in range(int(input())):
    graph = defaultdict(list)
    v = int(input())
    e = int(input())
    for i in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    print('T' if dfs(0, {}, 0) else 'F')