n, s = map(int,input().split())
lst = list(map(int,input().split()))
left = 0
max_sum = 0
min_len = float('inf')
for right in range(n):
    max_sum += lst[right]
    while max_sum >= s:
        max_sum -= lst[left]
        min_len = min(min_len, right - left + 1)
        left += 1

print(min_len if min_len != float('inf') else 0)