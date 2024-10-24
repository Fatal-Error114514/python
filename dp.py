def dp(score, day, max_time):
    s = len(score)
    table = [[0 for i in range(max_time + 1)] for i in range(s + 1)]
    for i in range(s + 1):
        for j in range(max_time + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif day[i - 1] <= j:
                table[i][j] = max(score[i - 1] + table[i - 1][j - day[i -1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    return table[s][max_time]

max_time = 2*2
score = [7, 6, 9, 9, 8]
day = [int(0.5*2), int(0.5*2), int(1*2), int(2*2), int(0.5*2)]
print(dp(score, day, max_time))