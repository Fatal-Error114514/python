def knapsack(s):
    data = s.split()
    n = int(data[0])
    exp = [int(i) for i in data[2::3]]
    wei = [int(i) for i in data[3::3]]
    lst = [0 for i in range(n+1)]

    for i in range(len(exp)):
        for kg in range(n, wei[i]-1, -1):
            lst[kg] = max(lst[kg], exp[i] + lst[kg-wei[i]])
    print(lst[-1])


knapsack("4 電視 40000 3 音響 50000 4 筆電 20000 1 手機 25000 1")