n=int(input())
if n==1 or n%2==0:
    print("請輸入比1大的奇數")
else:
    list=[[" " for i in range(n)] for i in range(n)]    #for 控制串列的數量
    for i in range(n):
        for j in range(n):
            if i==j:
                list[i][j]="*"
            list[i][n-1-i]="*"

    for i in list:
        for j in i:
            print(j,end="")
        print()