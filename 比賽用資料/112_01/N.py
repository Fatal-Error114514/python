month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30] # 已過天數
day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for _ in range(int(input())):
    m, d = map(int,input().split())
    d -= 1  # 要從第0天開始算
    for i in range(m):
        d += month[i]
    print(day[d % 7])