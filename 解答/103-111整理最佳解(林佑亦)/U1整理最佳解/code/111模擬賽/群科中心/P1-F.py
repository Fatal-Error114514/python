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
def genTestData(dataSize = 100):
    random.seed()
    sample = []
    for _ in range(0, dataSize):
        t = []
        t.append(random.randint(100, 65536))
        t.append(random.randint(5, 10))
        sample.append(t)
    with open(filename, "w", newline='\n') as f:
        f.write(f"{dataSize}\n")
        for t in sample:
            f.write(f'{t[0]} {t[1]}\n')

genTestData(10)


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

l = 10 ** 11
fib = [0, 1, 1, 1]
for k in range(4, 65535):
    fib.append((fib[k-3]+fib[k-2]+fib[k-1]) % l)

for i in range(n):
    n, m = [int(t) for t in inf.pop(0).split()]
    print(str(fib[n])[-m:])

# 主要程式結束
if infile is not sys.stdin:
    infile.close()
    end = datetime.datetime.now()
    print("執行時間:", end - start, "秒")

    with open(filename, "r") as infile:
        with open(outfile, "w", newline='\n') as wf:
            n = int(infile.readline())
            inf = infile.read().splitlines()
            l = 10 ** 11
            fib = [0, 1, 1, 1]
            for k in range(4, 65535):
                fib.append((fib[k - 3] + fib[k - 2] + fib[k - 1]) % l)
            for i in range(n):
                n, m = [int(t) for t in inf.pop(0).split()]
                ans = str(fib[n])[-m:]
                wf.write(f"{ans}\n")

