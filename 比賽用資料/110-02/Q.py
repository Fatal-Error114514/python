from heapq import heapify, heappop, heappush

n = int(input())
heap = list(map(int,input().split()))
heapify(heap)
ans = 0
while len(heap) > 1:
    a = heappop(heap) + heappop(heap)
    ans += a
    heappush(heap, a)
print(ans)