for _ in range(int(input())):
    x,n=map(int,input().split())
    k=0
    ans=0
    for i in sorted(map(int,input().split()),reverse=True):
        k+=1
        if k*i>=n:
            ans+=1
            k=0
    print(ans)