def knapsack(s):
    s = s.split()

    n = int(s[0])
    kg = [int(i) for i in s[3::3]]
    exp = [int(i) for i in s[2::3]]
    
    lst = [[0]*(n+1) for i in range ((len(kg)+1))]
    for i in range(len(kg)): # 0~3 (四樣物品)
        for j in range(1, n+1): # 1~4公斤
            if(kg[i] <= j):
                lst[i+1][j] = max(lst[i][j], exp[i] + lst[i][j-kg[i]])
            else:
                lst[i+1][j] = lst[i][j]

    print(lst[-1][-1])
    
knapsack("4 電視 40000 3 音響 50000 4 筆電 20000 1 手機 25000 1")