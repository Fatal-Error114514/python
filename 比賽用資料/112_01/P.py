from heapq import heapify, heappop, heappush

input()
nodes = {}
lst = list(map(int,input().split()))
temp = lst.copy()
heapify(temp)
while len(temp) > 1:
    a, b = heappop(temp), heappop(temp)
    num = a + b
    nodes[a] = num
    nodes[b] = num
    heappush(temp, num)
codes = []
root = temp[0]
for i in lst:
    count = 0
    while i != root:
        i = nodes[i]
        count += 1
    codes.append(count)
print(sum(codes))