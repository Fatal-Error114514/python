# https://zerojudge.tw/ShowProblem?problemid=e544
def COUNT(lst):
    count = 0
    for i in range(1,len(lst)):
        for j in range(i):
            if(ord(lst[j]) > ord(lst[i])):
                count += 1
    return count

n = int(input())
for _ in range(n):
    x = input()
    x = list(map(int,input().split()))  #x[0]=lst長度  x[1]=幾行比較
    Lst = []
    SortList = []
    for i in range(x[1]):
        Lst.append(input())               #存資料順序
        SortList.append(COUNT(Lst[i]))    #排資料順序
    printf = sorted(SortList)
    for i in printf:
        print(Lst[SortList.index(i)])
        SortList[SortList.index(i)] = 'X'  #把用完的指標打XX