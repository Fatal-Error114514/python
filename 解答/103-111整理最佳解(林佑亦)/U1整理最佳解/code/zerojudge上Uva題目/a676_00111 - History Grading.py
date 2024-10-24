# https://zerojudge.tw/ShowProblem?problemid=a676
# 這題很賤，我也被騙... 這有解說https://zerojudge.tw/ShowThread?postid=10963&reply=0

n = int(input()) +1
ans = None
while True:
    try:
        temp = list(map(int, input().split()))
        temp.insert(0, 0)
        lst = temp.copy()
        for i, j in enumerate(temp):
            lst[j] = i
        if(not ans):
            ans = lst.copy()
            continue
                    
        table = [[0] * (n) for i in range(n)]
 
        for i in range(1, n):
            for j in range(1, n):
                if(ans[i] == lst[j]):
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        print(table[-1][-1])
    except:
        break