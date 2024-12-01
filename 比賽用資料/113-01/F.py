from collections import Counter
n = int(input())
count = Counter()
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        count[i] += 1
        n //= i
if n != 1: count[n] = 1
ans = [f'{i}^{j}' if j > 1 else f'{i}' for i, j in count.items()]
print(*ans, sep = ' * ')