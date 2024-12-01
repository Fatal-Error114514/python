lst = []
for _ in range(int(input())):
    x, y = map(int,input().split())
    lst.append((x, y))
ans = []
for i in range(len(lst) - 1):
    ans.append(abs(lst[i][0] - lst[i + 1][0]) + abs(lst[i][1] - lst[i + 1][1]))
print(max(ans), min(ans))