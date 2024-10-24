for i in range(int(input())):
    
    n,limit=map(int,input().split())
    group=list(map(int,input().split()))
    ans=0
    count=1
    
    for j in sorted(group,reverse=True):    #遞減排序後，最小值一定為j
        
        if count*j>=limit:
            ans+=1
            count=0
        
        count+=1
    
    print(ans)