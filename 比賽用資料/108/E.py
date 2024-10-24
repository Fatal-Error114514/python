from collections import Counter

for _ in range(int(input())):
    times, l = map(int,input().split())
    lst = []
    for i in range(times):
        lst.append(input())

    lst = list(zip(*lst))
    DNA = ['A', 'C', 'G', 'T']
    output = []

    for i in lst:
        x = 'Z'
        for j in DNA:
            if i.count(j) > i.count(x):
                x = j
        output.append(x)
    print(*output, sep = '')