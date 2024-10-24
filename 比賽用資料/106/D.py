from itertools import permutations

for _ in range(int(input())):
    i, j, k = map(str, input().split(','))
    s1 = list(permutations(i, len(i)))[int(j) - 1]
    s2 = list(permutations(i, len(i)))[int(k) - 1]
    a, b = 0, 0
    for n in range(len(i)):
        if s1[n] == s2[n]:
            a += 1
        elif s2[n] in s1:
            b += 1
    print(f'{a}A{b}B')