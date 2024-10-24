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
def genTestData(dataSize = 100, min_bags_num = 5, max_bags_num = 20):
    random.seed()
    sample = []
    for _ in range(dataSize):
        random.seed()
        l = random.randint(min_bags_num, max_bags_num+1) * 2
        e = []
        for j in range(l):
            t = [0, 0]
            t[0] = random.randint(1, 100001)
            t[1] = random.randint(1, 100001)
            e.append(t)
        sample.append(e)

    with open(filename, "w", newline='\n') as f:
        f.write(f"{dataSize}\n")
        for t in sample:
            f.write(f'{t}\n')

genTestData(10, 100, 500)

import sys
import datetime
import bisect
import ast

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
    bags = ast.literal_eval(inf.pop(0))
    bags.sort(key=lambda x: (x[0], -x[1]))
    res = []
    for _, h in bags:
        idx = bisect.bisect_left(res, h)
        if idx == len(res):
            res.append(h)
        else:
            res[idx] = h
    print(len(res))

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
                bags = ast.literal_eval(inf.pop(0))
                bags.sort(key=lambda x: (x[0], -x[1]))
                res = []
                for _, h in bags:
                    idx = bisect.bisect_left(res, h)
                    if idx == len(res):
                        res.append(h)
                    else:
                        res[idx] = h
                wf.write(f"{len(res)}\n")