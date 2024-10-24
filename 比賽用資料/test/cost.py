from heapq import heapify,heappush,heappop

for _ in iter(input,'0'):
  heap=list(map(int,input().split()))
  heapify(heap)

  ans=0
  while len(heap)>1:
    s=heappop(heap)+heappop(heap)   #取出最小的兩個成本相加，並將相加後的數字放回容器
    ans+=s
    heappush(heap,s)
  print(ans)