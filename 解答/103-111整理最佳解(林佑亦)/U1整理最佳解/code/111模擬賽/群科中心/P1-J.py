# 本程式由 三重商工 資料處理科 林易民老師 撰寫
# 本程式的寫法，選手只要將測試資料所在的檔名寫入
# 到下面的filename變數中，程式就會讀取filename變數中的
# 中檔案的測試資料。如果要上傳到Domjudge評分，只要
# 設定  filename="" 就可上傳評分
# genTestData會自動產生測試資料的輸入檔
# 只要filename、outfile中有檔名，
# 然後執行genTestData就會自動產生測試資料的輸出入檔
# 本題還會針對每個樹產生對應的圖檔，放在同一個目錄下
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import ast
import collections

filename = "1.in" #測試資料輸入檔名
outfile = "1.ans"  #測試資料輸出檔名

#產生測試資料-輸入檔
def get_tree(S):
    n = len(S)
    L = set(range(1, n+2+1))
    tree_edges = []
    for i in range(n):
        u, v = S[0], min(L - set(S))
        S.pop(0)
        L.remove(v)
        tree_edges.append((u,v))
    tree_edges.append((L.pop(), L.pop()))
    return tree_edges

def hierarchy_pos(G, root, levels=None, width=1., height=1.):
    TOTAL = "total"
    CURRENT = "current"
    def make_levels(levels, node=root, currentLevel=0, parent=None):        
        if not currentLevel in levels:
            levels[currentLevel] = {TOTAL : 0, CURRENT : 0}
        levels[currentLevel][TOTAL] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            if not neighbor == parent:
                levels =  make_levels(levels, neighbor, currentLevel + 1, node)
        return levels

    def make_pos(pos, node=root, currentLevel=0, parent=None, vert_loc=0):
        dx = 1/levels[currentLevel][TOTAL]
        left = dx/2
        pos[node] = ((left + dx*levels[currentLevel][CURRENT])*width, vert_loc)
        levels[currentLevel][CURRENT] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            if not neighbor == parent:
                pos = make_pos(pos, neighbor, currentLevel + 1, node, vert_loc-vert_gap)
        return pos
    if levels is None:
        levels = make_levels({})
    else:
        levels = {l:{TOTAL: levels[l], CURRENT:0} for l in levels}
    vert_gap = height / (max([l for l in levels])+1)
    return make_pos({})

def savepic(edge,picname,start=1):
    g = nx.Graph()
    g.add_edges_from(edge)
    pos = hierarchy_pos(g, start)
    nx.draw(g, pos=pos, with_labels=True, node_color='white',  edgecolors='black', node_size=1000, width=3, font_size=10)
    plt.savefig(picname)
    plt.clf()

def genTestData(datasize = 100, minnodenum =2, maxnodenum=5, start=1):
    random.seed()
    sample = []
    O_E = ['奇數', '偶數']
    for i in range(datasize):
        n = random.randint(minnodenum, maxnodenum) # n: 節點
        S = np.random.choice(range(1, n + 1), n - 2, replace=True).tolist()
        T_E = get_tree(S)  # the spanning tree corresponding to S
        e = []
        for t in T_E:
            e.append([t[0]+(start-1), t[1]+(start-1)])
        sample.append(e)
    with open(filename, "w", newline='\n') as f:
        f.write(f"{datasize}\n")
        counter = 0
        for t in sample:
            counter = counter + 1
            f.write(f'{t}\n')
            savepic(t, f"pic{counter}.png", start)

def dfs(g, ans, count, node=0, parent=None):
    for child in g[node]:
        if child != parent:
            dfs(g,ans, count, child, node)
            count[node] = count[node] + count[child]
            ans[node] = ans[node] + ans[child] + count[child]


def dfs2(g, ans, count, node=0, parent=None):
    for child in g[node]:
        if child != parent:
            ans[child] = ans[node] - count[child] + N - count[child]
            dfs2(g, ans, count, child, node)

genTestData(20 ,minnodenum=10, maxnodenum=15, start=0)

import sys
import datetime

start = datetime.datetime.now()
if filename:
    infile = open(filename)
else:
    infile = sys.stdin
n = int(infile.readline())
inf = infile.read().splitlines()
# 主要程式開始
# 本程式由 三重商工 資料處理科 林易民老師 撰寫

for i in range(n):
    edges = ast.literal_eval(inf.pop(0))
    graph = collections.defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    N = len(graph.keys())
    count = [1] * N
    ans = [0] * N
    dfs(graph, ans, count, 0)
    dfs2(graph, ans, count, 0)
    print(sum(ans))

# 主要程式結束
if infile is not sys.stdin:
    infile.close()
    end = datetime.datetime.now()
    print("執行時間:", end - start, "秒")

    with open(filename, "r") as infile:
        with open(outfile, "w", newline='\n') as wf:
            n = int(infile.readline())
            inf = infile.read().splitlines()
            for i in range(n):
                edges = ast.literal_eval(inf.pop(0))
                graph = collections.defaultdict(set)
                for u, v in edges:
                    graph[u].add(v)
                    graph[v].add(u)
                N = len(graph.keys())
                count = [1] * N
                ans = [0] * N
                dfs(graph, ans, count, 0)
                dfs2(graph, ans, count, 0)
                wf.write(f"{sum(ans)}\n")
