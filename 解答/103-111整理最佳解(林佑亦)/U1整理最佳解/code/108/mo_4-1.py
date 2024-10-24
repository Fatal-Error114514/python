from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = int(Input())
dic = [[] for i in range(n+1)]
leaf = []
root = [i for i in range(1, n+1)]
check = set()
for i in range(1, n+1):
    x = list(map(int,Input().split()))[1:]
    if(x):
        dic[i] = x
        check = check | set(x)
    else:
        leaf.append(i)
root = list(set(root) - check)[0]
print(root)
high = [[] for i in range(n+1)]
high[root] = 1
queue = [root]
while(len(queue)):
    p = queue.pop()
    for i in dic[p]:
        queue.append(i)
        high[i] = high[p] +1
temp = []
for i in leaf:
    temp.append(high[i])
print(max(temp))
