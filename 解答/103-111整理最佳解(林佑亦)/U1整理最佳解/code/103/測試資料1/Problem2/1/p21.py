from sys import stdin
n = int(stdin.readline())
for h in range(n):
    a = stdin.readline().strip()
    b = stdin.readline().strip()
    s = set()
    for i in a:
        for j in b:
            if i == j:
                s.add(i)
    s = list(s)
    s.sort()
    if s == []:
        print("N")
    else:
        print("".join(i for i in s))