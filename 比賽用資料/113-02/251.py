s1 = input()
s2 = input()
long = 0
table = [[0 for i in range(len(s1) + 1)] for i in range(len(s2) + 1)]
for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):
        if s1[j - 1] == s2[i - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
            if table[i][j] > long:
                long = table[i][j]
print(long)