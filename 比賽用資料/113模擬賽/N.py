m, n, w = map(int,input().split())
value = list(map(int,input().split()))
order = []
for i in range(n):
    a, b = map(int,input().split())
    order.append((value[a - 1] * b, b))

table = [0 for i in range(w + 1)]
for i in order:
    for j in range(w, i[1]-1, -1):
        table[j] = max(table[j], i[0] + table[j - i[1]])
print(table[-1])