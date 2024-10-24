n = int(input())
parent = {} # 父節點編號
degree = {} # 幾個子節點
depth = {} # 深度
height = {} # 高度
dic = {} # 有那些子節點
leaf = [] # 記錄葉節點
root = None
for i in range(n):
    node,l,r = map(int,input().split())
    dic[node] = []
    height[node] = 0
    count = 0
    if(root == None):
        root = node
        parent[node] = -1
        depth[node] = 0
    if(l != -1):
        parent[l] = node
        dic[node].append(l)
        count += 1
    if(r != -1):
        parent[r] = node
        dic[node].append(r)
        count += 1
    if(len(dic[node]) == 0): # 如果是葉節點
        leaf.append(node)
    degree[node] = count

#depth
queue = [root]
while queue:
    p = queue.pop(0)
    for i in dic[p]:
        depth[i] = depth[p] +1
        queue.append(i)

#height
for i in leaf:
    while(i != root):
        pa = parent[i]
        height[pa] = max(height[pa], height[i] + 1)
        i = pa

for i in range(n):
    print(f'node {i}: parent = {parent[i]}, degree = {degree[i]}, depth = {depth[i]}, height = {height[i]},')
    