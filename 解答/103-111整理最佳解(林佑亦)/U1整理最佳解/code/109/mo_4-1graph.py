""""
程式概念:
1. 先將一般的圖形(graph)，依照DFS轉換成二元樹，保證每個節點都只有一個父節點，方便程式計算。
2. 主要原則: 

(1) 若該節點為樹根(root)，只要他有兩個子節點，就是關節點; 
(2) 依照DFS走訪二元樹時，自己(V)的父節點一定會先被走訪，所以在檢查和V有連結的節點時，若發現已經走訪過，表示他為V的父節點；若未走訪，則代表為V的子節點
(3) 承(2)，計算自己有連結到的所有父節點的距離(但需去除自己直屬父節點，因為要找別的路線)，若「從root經過自己有連結的父節點」 < 「原本DFS的順序(距離)」，
    則代表有其他替代路線(更近的路線)；反之則沒有，代表該節點便是關節點。
(4) 遞迴的概念就是，每個節點都要當過root來就算結果。每個root的最短距離為：取 底下所有子節點的最小距離值 (如果你的子節點跟更上面的父節點有路徑時，
    距離比較短，代表有替代路線，就絕對不可能是關節點)

範例：
6
2 1 3
5 4 6 2 
0
0

建立串列：
[[0], [1, 2], [2, 1, 3, 5], [3, 2], [4, 5], [5, 4, 6, 2], [6, 5]]

每個節點所連線的節點:
1->2
2->1,3,5
3->2
4->5
5->2,4,6
6->5
"""

from sys import stdin

# 建立 adjacency array
def adjArray(n):
    result = [[i] for i in range(n+1)]
    line = stdin.readline().split()
    while line[0] != '0':
        line = list(map(int, line))
        for i in range(1, len(line)):
            if line[i] not in result[line[0]]:
                result[line[0]].append(line[i])
            if line[0] not in result[line[i]]:
                result[line[i]].append(line[0])
        line = stdin.readline().split()
    return result


# 深度搜尋
def DFS(P, V):
    global t
    Visted[V] = t   # 將當前節點V，設定走訪順序
    low[V] = t      # 將當前節點V，預設能到到達最高的父節點為自己
    t += 1          # 控制走訪順序
    child = 0       # 計算當前節點V，有幾個子節點
    ans = False     # 預設當前節點V，不是關節點
    for i in range(1, len(result[V])):   # 從節點V開始走訪，有直接連結的其他節點，i只是編號
        node = result[V][i]              # 取得節點V，連結到的其他節點 (node)，node是值
        if P != node:                   # node不能為根節點 (根節點沒有父節點，因此只要有2個以上子節點，便是關節點)，也代表不走回頭路(不包含自己直屬的父節點)
            if Visted[node]:             # 節點node若「已」走訪過，代表node為父節點，因為採DFS關係父節點一定會先被走訪過。
                low[V] = min(low[V], Visted[node])   # 因此必須更新，節點V與每個可到達的父節點，取最短距離。 (如果有更短距離，表示有其他替代路線) 
            else:                        # 節點node「尚未」走訪過，代表node為子節點
                child += 1               # 計算節點V的子節點個數
                DFS(V, node)             # 每個節點(node)都要當過樹根(root)，因此其餘節點遞迴做同樣動作(找節點V與每個可到達的父節點，取最短距離)
                low[V] = min(low[V], low[node])   # 節點V的最短距離為，底下所有子節點的最短路徑。(因為如果底下的子節點，若有其他路線連到更倒個父節點，則代表有替代路線)
               
                if low[node] >= Visted[V]:        # 若子節點的最短路徑 >=　DFS走訪距離，表示沒有替代路徑，刪除掉他，則會造成圖形不連通，稱為關節點。
                    ans = True
    if ((V == P) and (child > 1)) or ((V != P) and (ans == True)):
        ap[V] = 1


# 主程式
n = stdin.readline().split()
while n != ['0']:
    n = int(n[0])
    result = adjArray(n)  # 建立圖形
    Visted = [0] * (n+1)  # 儲存每個節點的走訪順序
    low = [0] * (n+1)     # 儲存每個節點，取 自己可以到達的所有父節點中的最小值 (不包含自己直屬的父節點，因為不走回頭路，或者說計算走同一條路沒有意義)
    ap = [0] * (n+1)      # 儲存哪些節點是關節點
    t = 1                 # 計算走訪順序
    DFS(1, 1)
    print("result:",result)
    print("Visted:",Visted)
    print("low:",low)
    print("ap:",ap)
    print(sum(ap))
    n = stdin.readline().split()