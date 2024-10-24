# https://zerojudge.tw/ShowProblem?problemid=a539
# 跟抱怨值一樣
while True:
    try:
        input()
        lst = list(map(int,input().split()))
        count = 0
        for i in range(1, len(lst)):
            for j in range(i):
                if(lst[j] > lst[i]):
                    count += 1
        print('Minimum exchange operations :',count)
    except EOFError:
        break