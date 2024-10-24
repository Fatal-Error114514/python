n = int(input())
while n:
    lst = []
    for i in range(n):
        lst.append(int(input()))
    count = 0
    for i in range(1, len(lst)):
        for j in range(i, -1, -1):
            if(lst[j] > lst[i]):
                count += 1
    print(count)
    n = int(input())
