for _ in range(int(input())):
    n = int(input())
    path = [0 for i in range(n + 1)]    #紀錄path[node]連結到的點，類defaultdict的寫法
    ans = [0 for i in range(n + 1)]     #紀錄每個節點的距離
    for i in range(n):
        a, b = map(int,input().split())
        path[a] = b

    for i in range(1, n + 1):
        node = i
        check = [0 for i in range(n + 1)]   #檢查走過的地方有沒有再被走到，類似著色問題
        while check[node] != 1:
            check[node] = 1
            node = path[node]
        ans[i] = sum(check)

    print(ans.index(max(ans)))