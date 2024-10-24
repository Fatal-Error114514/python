from collections import defaultdict


def dfs(node, prev=None, k=0):
    # 到葉子了 注意，這還是樹只是弄成無向圖而已，因此只有parent的即是葉子
    if graph[node] == [prev]: return k, node
		m = k, node
    for x in graph[node]:
        if x != prev:
            m = max(m, dfs(x, node, k + 1))
    return m


graph = defaultdict(list)

for _ in range(int(input()) - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 最長距離 = 圖中任一點 a 的最遠點 b，b 到最遠點的距離
_, a = dfs(1)
k, _ = dfs(a)

print(k)