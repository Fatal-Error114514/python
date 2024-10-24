a, b, c = input(), input(), input()
e, f, g = len(a), len(b), len(c)
lcs = [[[0] * (g + 1) for _ in range(f + 1)] for _ in range(e + 1)]

for i in range(e):
    for j in range(f):
        for k in range(g):
            if a[i] == b[j] == c[k]:
                lcs[i + 1][j + 1][k + 1] = lcs[i][j][k] + 1
            else:
                lcs[i + 1][j + 1][k + 1] = max(lcs[i + 1][j + 1][k], lcs[i + 1][j][k + 1], lcs[i][j + 1][k + 1])

print(lcs[e][f][g])