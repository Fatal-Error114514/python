a, b = input(), input()
m, n = len(a), len(b)

dp = [[max(i, j) for j in range(n + 1)] for i in range(m + 1)]

for i, c1 in enumerate(a):
    for j, c2 in enumerate(b):
        if c1 == c2:
            dp[i + 1][j + 1] = dp[i][j]
        else:
            dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1

print(dp[-1][-1])