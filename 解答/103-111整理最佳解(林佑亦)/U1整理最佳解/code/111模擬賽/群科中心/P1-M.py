# 本程式由 三重商工 資料處理科 林易民老師 撰寫
# 本程式的寫法，選手只要將測試資料所在的檔名寫入
# 到下面的filename變數中，程式就會讀取filename變數中的
# 中檔案的測試資料。如果要上傳到Domjudge評分，只要
# 設定  filename="" 就可上傳評分
# genTestData會自動產生測試資料的輸入檔
# 只要filename、outfile中有檔名，
# 然後執行genTestData就會自動產生測試資料的輸出入檔
import random
filename = "" #測試資料輸入檔名
outfile = "1.ans"  #測試資料輸出檔名
#產生測試資料-輸入檔
def genTestData(dataSize = 100, minN=30, maxN=60, minM = 30, maxM=60, minNum=1, maxNum = 65535):
    random.seed()
    with open(filename, "w", newline='\n') as f:
        f.write(f"{dataSize}\n")
        for _ in range(dataSize):
            M = random.randint(minM, maxM)
            N = random.randint(minN, maxN)
            f.write(f"{N}\n")
            f.write(f"{M}\n")
            for _ in range(N):
                t = [ str(random.randint(minNum, maxNum))  for _ in range(M)]
                l = " ".join(t)
                f.write(f"{l}\n")

genTestData(10, 30, 50, 30, 50, 1, 65535)

import sys
import datetime
import heapq

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
    R = int(inf.pop(0))
    C = int(inf.pop(0))
    grid = []
    for _ in range(R):
        grid.append([int(c) for c in inf.pop(0).split()])
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    heap = []
    ans = grid[0][0]
    visited = [[False] * C for _ in range(R)]
    heapq.heappush(heap, (-grid[0][0], 0, 0))
    visited[0][0] = True
    while heap:
        cur_val, cur_row, cur_col = heapq.heappop(heap)
        ans = min(ans, grid[cur_row][cur_col])
        if cur_row == R - 1 and cur_col == C - 1:
            break
        for d_row, d_col in dirs:
            new_row = cur_row + d_row
            new_col = cur_col + d_col
            if -1 < new_row < R and -1 < new_col < C and not visited[new_row][new_col]:
                heapq.heappush(heap, (-grid[new_row][new_col], new_row, new_col))
                visited[new_row][new_col] = True
    print(ans)

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
                R = int(inf.pop(0))
                C = int(inf.pop(0))
                grid = []
                for _ in range(R):
                    grid.append([int(c) for c in inf.pop(0).split()])
                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                heap = []
                ans = grid[0][0]
                visited = [[False] * C for _ in range(R)]
                heapq.heappush(heap, (-grid[0][0], 0, 0))
                visited[0][0] = True
                while heap:
                    cur_val, cur_row, cur_col = heapq.heappop(heap)
                    ans = min(ans, grid[cur_row][cur_col])
                    if cur_row == R - 1 and cur_col == C - 1:
                        break
                    for d_row, d_col in dirs:
                        new_row = cur_row + d_row
                        new_col = cur_col + d_col
                        if -1 < new_row < R and -1 < new_col < C and not visited[new_row][new_col]:
                            heapq.heappush(heap, (-grid[new_row][new_col], new_row, new_col))
                            visited[new_row][new_col] = True
                wf.write(f"{ans}\n")