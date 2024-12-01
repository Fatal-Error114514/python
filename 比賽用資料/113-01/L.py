n = int(input())
lst = list(map(int,input().split()))
ans = - float('inf')
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += lst[j]
        ans = max(temp, ans)
print(ans)