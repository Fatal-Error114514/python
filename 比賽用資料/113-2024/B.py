a, b = map(int,input().split())
a, b = sorted([a, b])
ans = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        ans += i
print(ans)