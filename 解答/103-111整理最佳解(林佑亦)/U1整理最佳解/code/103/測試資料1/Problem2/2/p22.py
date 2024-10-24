from sys import stdin
n = int(stdin.readline())
for h in range(n):
    a = list(map(int,stdin.readline().strip().split()))
    b = list(map(int, stdin.readline().strip().split()))
    a.pop(0)
    b.pop(0)
    print(len(set(a)&set(b)))