from collections import defaultdict

def dfs(prev, node):
    if node in visited: return node
    visited.add(node)
    for n in graph[node]:
        if n == prev: continue
        loop = dfs(node, n)
        if loop: return loop            #尋找迴圈

def floop(loop, prev, node, path):
    if prev is not None and loop == node: return path
    for n in graph[node]:
        if n == prev: continue
        p = floop(loop, node, n, path + [node])
        if p: return p

for _ in range(int(input())):
    graph = defaultdict(list)
    s = input().split()
    start = None        #起始點
    for i in s:
        a, b = map(int, i.split(','))
        if not start: start = a
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    loop = dfs(None, start)
    if not loop:
        if len(graph) == len(visited):
            print('T')
        else:
            print('F')
    else:
        print(*sorted(floop(loop, None, loop, [])), sep = ', ')