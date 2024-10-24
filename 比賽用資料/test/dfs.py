from collections import defaultdict
def dfs(node,prev=None,k=0):
    if graph[node]==[prev]:return k,node
    m=k,node
    for x in graph[node]:
        if x!=prev:
            m=max(m,dfs(x,node,k+1))
    return m
graph=defaultdict(list)
for _ in range(int(input())-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

_,a=dfs(1)
k,_=dfs(a)

print(k)