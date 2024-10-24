n = int(input())
d, s = 0, 0

while n:
    if n % 2:
        n, s = n - 1, s + 1
    else:
        n, d = n // 2, d + 1

print(2 * d + s)
