for _ in range(int(input())):
    j, k = map(str, input().split(', '))
    a, b = 0, 0
    for i in range(len(j)):
        if j[i] == k[i]:
            a += 1
        elif j[i] in k:
            b += 1
    print(f'{a}A{b}B')