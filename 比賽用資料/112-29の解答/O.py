n, m = map(int, input().split())
k = n // 2
xs = tuple(map(int, input().split()))

for _ in range(m):
    xs = sum(zip(xs[:k], xs[k:]), ())
print(*xs)
