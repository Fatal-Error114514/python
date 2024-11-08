def LIS(lst):
    table = [1] * len(lst)
    ind = [i for i in range(len(lst))]
    for i in range(len(lst)):
        for j in range(i):
            if lst[j] < lst[i]:
                if table[j] + 1 > table[i]:
                    table[i] = table[j] + 1
                    ind[i] = j
    print(max(table))

    max_ind = table.index(max(table))
    lis = []
    while max_ind != ind[max_ind]:
        lis.append(lst[max_ind])
        max_ind = ind[max_ind]
    lis.append(lst[max_ind])
    print(lis[::-1])

input()
lst = list(map(int,input().split()))
LIS(lst)