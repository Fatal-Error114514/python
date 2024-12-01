n, x = map(int,input().split())
coin = list(map(int,input().split()))
table = [float('inf')] * (x + 1)
table[0] = 0
for c in coin:
    for i in range(c, x + 1):
        table[i] = min(table[i], table[i - c] + 1)
print(table[x] if table[x] != float('inf') else -1)