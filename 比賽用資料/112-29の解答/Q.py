from heapq import heapify, heappop, heappush


for _ in iter(input, '0'):
    heap = list(map(int, input().split()))
    heapify(heap)
    cost = 0
    while len(heap) > 1:
        c = heappop(heap) + heappop(heap)
        heappush(heap, c)
        cost += c
    print(cost)
