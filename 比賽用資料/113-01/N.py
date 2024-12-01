def dp(n):
    table = [0] * (n + 1)
    table[0] = 1
    curr_sum = table[0]
    for i in range(1, n + 1):
        table[i] = curr_sum % mod
        curr_sum += table[i]

        if i >= 6:
            curr_sum -= table[i - 6]    # 超出骰子的最大點數，移除舊值

    return table[n]
n = int(input())
mod = 10 ** 9 + 7
print(dp(n))