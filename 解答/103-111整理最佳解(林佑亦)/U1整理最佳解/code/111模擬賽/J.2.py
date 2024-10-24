def dfs(g, ans, count, node=0, parent=None):
    for child in g[node]:
        if child != parent:
            dfs(g,ans, count, child, node)
            count[node] = count[node] + count[child]
            ans[node] = ans[node] + ans[child] + count[child]


def dfs2(g, ans, count, node=0, parent=None):
    for child in g[node]:
        if child != parent:
            ans[child] = ans[node] - count[child] + N - count[child]
            dfs2(g, ans, count, child, node)

from collections import defaultdict

for i in range(int(input())):
    edges = eval(input())
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    N = len(graph.keys())
    count = [1] * N
    ans = [0] * N
    dfs(graph, ans, count, 0)
    dfs2(graph, ans, count, 0)
    print(sum(ans))

