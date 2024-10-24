mapping = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(52)))

s = input()
n = len(s)
s_prime = list(map(mapping.get, s))

prev, ans = -1, 0
k = 0
for curr in s_prime:
    if prev < curr:
        prev, k = curr, k + 1
    else:
        ans = max(ans, k)
        prev, k = curr, 1

print(max(ans, k))
