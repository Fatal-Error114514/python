def dp(m, coin):
    table = [0 for i in range(m + 1)]
    table[0] = 1

    for i in coin:
        for j in range(i, m + 1):
            table[j] += table[j - i]
    return table[m]

n, m = map(int,input().split())
coin = list(map(int,input().split()))
print(dp(m, coin))