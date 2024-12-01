from collections import defaultdict

def dfs(prev, node, height):
    max_n = node
    max_h = height
    for n in graph[node]:
        if n != prev:
            curr_n, curr_h = dfs(node, n, height + 1)
            if curr_h > max_h:
                max_h = curr_h
                max_n = curr_n
    return max_n, max_h

graph = defaultdict(list)
for _ in range(int(input()) - 1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
x, _ = dfs(None, 1, 0)
p, h = dfs(None, x, 0)
print(h)