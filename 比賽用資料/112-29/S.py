from collections import defaultdict

def getsubgraph(x, subgraph):
    subgraph.add(x)
    
    for j in connection[x]:
        if j not in subgraph:
            subgraph |= getsubgraph(j, subgraph)
    
    return subgraph

n, m = map(int, input().split())

connection = defaultdict(list)
degrees = [0] *  n

for _ in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    connection[a].append(b)
    connection[b].append(a)
    degrees[a] += 1
    degrees[b] += 1

ans = 0
visited = set()

for i in range(n):
    if i in visited: continue
    subgraph = getsubgraph(i, set())
    ans += all(degrees[x] == 2 for x in subgraph)
    visited |= subgraph

print(ans)
