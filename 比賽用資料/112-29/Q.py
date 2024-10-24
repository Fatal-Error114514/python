from heapq import heappop,heappush,heapify

for i in iter(input,'0'):

    heap=list(map(int,input().split()))
    heapify(heap)
    ans=0

    while len(heap)>1:
        a=heappop(heap)+heappop(heap) #取出兩個最小值相加
        ans+=a
        heappush(heap,a)       #將相加後的數字放入heap
    print(ans)
