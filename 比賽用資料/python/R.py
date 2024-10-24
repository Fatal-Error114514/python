from collections import defaultdict
from typing import Tuple


# -> [level, node]
def dfs(node, prev = None, k = 0) -> Tuple[int, int]:
    return max(dfs(x, node, k + 1) for x in graph[node] if x != prev) if graph[node] != [prev] else (k, node)
        

graph = defaultdict(list)

for _ in range(int(input()) - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

_, a = dfs(1)
k, _ = dfs(a)

print(k)
