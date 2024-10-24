for _ in range(int(input())):
    num = [str(i) for i in range(10)]
    count = [0 for i in range(10)]
    for i in range(1, int(input()) + 1):
        for j in str(i):
            count[num.index(j)] += 1
    print(*count)