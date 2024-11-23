from heapq import heapify, heappop, heappush

n = int(input())
lst = [int(input()) for i in range(n)]
heapify(lst)
ans = 0
while len(lst) > 1:
    a, b = heappop(lst), heappop(lst)
    num = a + b
    heappush(lst,num)
    ans += num
print(ans)