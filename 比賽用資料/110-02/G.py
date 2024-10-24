ans = list(map(str,input().split()))

for _ in range(int(input())):
    n = list(map(str,input().split()))
    m = ans.copy()
    a = 0
    b = 0
    for i in range(4):
        if n[i] == m[i]:
            a += 1
            m[i] = n[i] = None
    for i in range(4):
        if m.count(n[i]) and n[i] != None:
            b += 1
            m[m.index(n[i])] = n[i] = None
    print(f'{a}A{b}B')