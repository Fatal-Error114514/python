from collections import defaultdict

def dfs(node, prev, height):
    max_height = height
    for child in graph[node]:
        if child == prev:
            continue
        curr_height = dfs(child, node, height + 1)
        max_height = max(max_height, curr_height)
    return max_height

graph = defaultdict(list)
n = int(input())
for _ in range(n - 1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    print(dfs(i, -1, 0), end = ' ')