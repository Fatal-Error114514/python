for _ in range(int(input())):
    arry = list(map(int,input().split()))
    for i in range(1, len(arry)):
        if arry[i - 1] > 0:
            arry [i] += arry [i - 1]
    print(max(arry))