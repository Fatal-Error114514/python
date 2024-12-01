a1, b1, c1 = map(int,input().split())
a2, b2, c2 = map(int,input().split())
n = int(input())
ans = - float('inf')
for x1 in range(n + 1):
    x2 = n - x1
    y1 = a1 * x1 ** 2 + b1 * x1 + c1
    y2 = a2 * x2 ** 2 + b2 * x2 + c2
    ans = max(y1+y2, ans)
print(ans)