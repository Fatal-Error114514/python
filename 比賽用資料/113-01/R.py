from collections import defaultdict

def dfs(node, parent):
    dp[node][0] = 0
    dp[node][1] = 0
    total = 0
    for n in graph[node]:
        if n != parent:
            dfs(n, node)
            total += max(dp[n][0], dp[n][1])
    dp[node][0] = total
    for n in graph[node]:
        if n != parent:
            dp[node][1] = max(dp[node][1], total - max(dp[n][1], dp[n][0]) + dp[n][0] + 1)
graph = defaultdict(list)
n = int(input())
dp = [[0, 0] for i in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1, -1)
print(max(dp[1][0], dp[1][1]))