from collections import Counter

n = input()
c = Counter()

for i in n:
    c[i] += 1

for x, y in sorted(c.items(), key = lambda x : (x[1], -ord(x[0]))):
    print(ord(x), y)
