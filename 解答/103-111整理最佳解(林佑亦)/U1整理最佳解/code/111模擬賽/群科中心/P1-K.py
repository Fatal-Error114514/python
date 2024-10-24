# 本程式由 三重商工 資料處理科 林易民老師 撰寫
# 本程式的寫法，選手只要將測試資料所在的檔名寫入
# 到下面的filename變數中，程式就會讀取filename變數中的
# 中檔案的測試資料。如果要上傳到Domjudge評分，只要
# 設定  filename="" 就可上傳評分
# genTestData會自動產生測試資料的輸入檔
# 只要filename、outfile中有檔名，
# 然後執行genTestData就會自動產生測試資料的輸出入檔
import random

filename = "1.in" #測試資料輸入檔名
outfile = "1.ans"  #測試資料輸出檔名
#產生測試資料-輸入檔
def genTestData(dataSize = 100, min_n_num=1, max_n_num=100, min_n=-10000, max_n=10000):
    random.seed()
    sample = []
    max_n = max_n + 1
    max_n_num = max_n_num + 1

    for i in range(dataSize):
        n = random.randint(min_n_num, max_n_num)
        t = []
        for j in range(n):
            t.append(str(random.randint(min_n, max_n)))
        sample.append(" ".join(t))

    with open(filename, "w", newline='\n') as f:
        f.write(f"{dataSize}\n")
        for t in sample:
            f.write(f'{t}\n')

genTestData(20, min_n_num=500, max_n_num=1000 )

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
    dp = [int(c) for c in inf.pop(0).split()]
    l, r, s, v = 0, 0, 0, dp[0]
    le = len(dp)
    for i in range(1, le):
        if dp[i-1] >= 0:
            dp[i] = dp[i-1]+dp[i]
        else:
            s = i
        if dp[i] > v:
            v = dp[i]
            l = start
            r = i
    ans = v
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
                dp = [int(c) for c in inf.pop(0).split()]
                l, r, s, v = 0, 0, 0, dp[0]
                le = len(dp)
                for i in range(1, le):
                    if dp[i - 1] >= 0:
                        dp[i] = dp[i - 1] + dp[i]
                    else:
                        s = i
                    if dp[i] > v:
                        v = dp[i]
                        l = start
                        r = i
                ans = v
                wf.write(f"{ans}\n")