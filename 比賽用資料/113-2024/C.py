triangle = [False] * 5
for _ in range(5):
    lst = sorted(list(map(int,input().split())))
    if lst[0] + lst[1] > lst[2]:
        triangle[_] = True
print(sum(triangle))