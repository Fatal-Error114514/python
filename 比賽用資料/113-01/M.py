a, b = 0, 1
mod = 10 ** 9 + 7
for i in range(2, int(input()) + 1):
    a, b = b, (a + b) % mod
print(b)