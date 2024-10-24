from collections import defaultdict

def get_subgraph(x,subgraph):
    subgraph.add(x)
    for y in connections[x]:
        if y not in subgraph:
            subgraph |= get_subgraph(y,subgraph)
    return subgraph

n,m=map(int,input().split())

connections = defaultdict(list)
degrees=[0]*n

for _ in range(m):
    a,b = [int(x) - 1 for x in input().split()]     #對準degrees的index
    connections[a].append(b)
    connections[b].append(a)
    degrees[a] +=1
    degrees[b] +=1

ans=0
visited=set()

for i in range(n):
    if i in visited: continue
    subgraph=get_subgraph(i,set())
    ans+= all(degrees[x]==2 for x in subgraph)
    visited |= subgraph

print(ans)