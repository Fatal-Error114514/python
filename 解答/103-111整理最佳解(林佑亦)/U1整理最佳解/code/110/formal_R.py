from sys import stdin
from collections import defaultdict

def Input():
    return stdin.readline().rstrip()

n,m = map(int,Input().split())
dic = defaultdict(list)
for i in range(m):
    a,b = map(int,Input().split())
    dic[a].append(b)

A,B = map(int,Input().split())
queue = [A]
visited = []
while(len(queue)):
    p = queue.pop(0)
    visited.append(p)
    for i in dic[p]:
        if(i == B):
            visited = queue = []
            break
        if(i not in visited):
            queue.append(i)
if(visited):
    print('No')
else:
    print('Yes')
