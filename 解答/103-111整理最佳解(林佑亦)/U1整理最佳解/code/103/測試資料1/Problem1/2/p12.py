from sys import stdin
n = int(stdin.readline())
for h in range(n):
    a,b,c,d = map(int,stdin.readline().split(","))
    # 5x*20y=110 x+y=10
    y = int((a*b-d)/(c-b))*-1
    x = int((d-c*y)/b)
    print(x,y,sep=",")