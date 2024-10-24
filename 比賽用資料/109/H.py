from collections import defaultdict

def dfs(graph, node, visited):
    visited[node] = True
    count = 1
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)
    
    return count

for _ in range(int(input())):
    graph = defaultdict(list)
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    max_count = 0
    best = 1
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        count = dfs(graph, i, visited)

        if count > max_count or count == max_count and i < best:
            max_count = count
            best = i
    print(best)