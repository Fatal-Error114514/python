from collections import defaultdict

n, m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a, b = map(int,input().split())
    d[a].append(b)

cta, ctb = map(int,input().split())
visited = []
queue = [cta]
while queue:
    node = queue.pop(0)
    visited.append(node)
    neighbors = d[node]
    for n in neighbors:
        if n == ctb:
            visited = queue = []
            break
        if n not in visited:
            queue.append(n)
if visited:
    print('No')
else:
    print('Yes')