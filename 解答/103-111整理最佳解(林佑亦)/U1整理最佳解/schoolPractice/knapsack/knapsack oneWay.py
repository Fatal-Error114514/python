def knapsack(s):
    s = s.split()

    n = int(s[0])
    kg = [int(i) for i in s[3::3]]
    exp = [int(i) for i in s[2::3]]
    
    lst = [0]*(n+1)
    for i in range(len(kg)): # 0~3 (四樣物品)
        for j in range(n, kg[i]-1, -1): # 4~1公斤
            lst[j] = max(lst[j], exp[i] + lst[j-kg[i]])
                
    print(lst[-1])
    
knapsack("4 電視 40000 3 音響 50000 4 筆電 20000 1 手機 25000 1")