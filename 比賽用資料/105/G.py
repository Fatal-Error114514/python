def lcs(text1, text2):
    m = len(text1)
    n = len(text2)
    table = [[0 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])
    return table[m][n]

for _ in range(int(input())):
    text1 = input()
    text2 = input()
    print(lcs(text1, text2))