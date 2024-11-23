lst = list(map(int,input().split()))
a = [0, 1, 2]
for i in range(3, max(lst) + 1):
    a.append(a[i - 3] - 2 * a[i - 2] + a[i - 1])
for i in lst:
    print(a[i] % 10)