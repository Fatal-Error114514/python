for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    k = 0
    for i in range(n):
        for j in range(i, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                k += 1
    print(f'Optimal train swapping takes {k} swaps.')