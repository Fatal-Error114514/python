def union(a, b):
    if sets[a] is None: sets[a] = {a}
    if sets[b] is None: sets[b] = {b}
    s1, s2 = sets[a], sets[b]

    if s1 is s2: return

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    s1 |= s2
    for x in s2:
        sets[x] = s1


n, v = map(int, input().split())
degrees = [0] * n
sets = [None] * n

for _ in range(v):
    a, b = [int(x) - 1 for x in input().split()]
    
    union(a, b)
    degrees[a] += 1
    degrees[b] += 1

ss = dict()
for s in sets:
    ss[id(s)] = s

if id(None) in ss:
    del ss[id(None)]

print(sum(all(degrees[x] == 2 for x in s) for s in ss.values()))
