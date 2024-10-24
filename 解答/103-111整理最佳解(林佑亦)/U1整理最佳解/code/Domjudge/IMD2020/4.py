price =   [0, 1, 5, 8, 9, 10, 12, 17, 20, 24, 25]
n = int(input())
table = [0] *(n+1)

for i in range(1, n+1):
    M = 0
    for j in range(1, i+1):
        M = max(M, price[j] + table[i-j])
    table[i] = M
print(table[i])
