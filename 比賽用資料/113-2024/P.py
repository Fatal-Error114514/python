import math
from collections import Counter

def mo_algorithm(n, arr, queries):
    # 每個區塊的大小
    block_size = int(math.sqrt(n))
    
    # 將查詢按照左端點所在的區塊排序，對於左端點在同一個區塊內的查詢，按照右端點排序
    queries.sort(key=lambda x: (x[0] // block_size, x[1]))
    
    # 初始化結果數組
    results = [0] * len(queries)
    current_l, current_r, current_answer = 0, 0, 0
    count = Counter()
    
    def add(x):
        nonlocal current_answer
        count[x] += 1
        if count[x] == 1:
            current_answer += 1
    
    def remove(x):
        nonlocal current_answer
        if count[x] == 1:
            current_answer -= 1
        count[x] -= 1
    
    for l, r, idx in queries:
        while current_r <= r:
            add(arr[current_r])
            current_r += 1
        while current_r > r + 1:
            current_r -= 1
            remove(arr[current_r])
        while current_l < l:
            remove(arr[current_l])
            current_l += 1
        while current_l > l:
            current_l -= 1
            add(arr[current_l])
        
        results[idx] = current_answer
    
    return results

n, q = map(int,input().split())
arr = list(map(int,input().split()))
queries = []
for i in range(q):
    a, b = map(int,input().split())
    queries.append((a - 1, b - 1, i))

results = mo_algorithm(n, arr, queries)

for result in results:
    print(result)