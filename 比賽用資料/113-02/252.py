s = list(input())
n = 0
if len(s) % 2 != 0: n = 1
for i in range(n, len(s), 2):
    s[i], s[i + 1] = s[i + 1], s[i]
print(''.join(s))