while True:
    try:
        lst = list(map(int,input()))
        if(len(lst) == 0):
            print(0)
        dp = [1] * len(lst)
        for i in range(len(lst)-1):
            if(lst[i+1] >= lst[i]):
                dp[i+1] = dp[i] + 1
        print(max(dp))
    except EOFError:
        break
