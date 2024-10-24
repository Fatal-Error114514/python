for _ in range(int(input())):
    s = list(map(list,input().split()))
    count = 0
    for i in s:
        if 's' in i or 'S' in i:
            count += 1
    print(count)