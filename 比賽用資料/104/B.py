n = int(input())
lotter = list(map(int,input().split(',')))
for _ in range(n):
    prize = [0, 0, 0, 0, 0, 0]
    g = list(map(int,input().split(',')))
    for i in range(len(g)):
        temp = g.copy()
        temp.pop(i)
        count = 0
        for j in temp:
            if j in lotter:
                count += 1
        if count > 1:
            prize[count - 1] += 1
    print(*prize[1:5], sep = ',')