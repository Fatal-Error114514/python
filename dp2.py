def dp(max_time, score, day):
    table = [0 for i in range(max_time + 1)]
    for i in range(len(score) + 1):
        for j in range(i, max_time + 1):
            table[j] = max(score[j - 1] + table[j - day[i - 1]], table[j -1])
    return table[max_time]

max_time = 2*2
score = [7, 6, 9, 9, 8]
day = [int(0.5*2), int(0.5*2), int(1*2), int(2*2), int(0.5*2)]
print(dp(max_time, score, day))