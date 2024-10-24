for i in range(int(input())):
    
    l=int(input())
    s=input()
    ans=1   #最少有一解

    for i in range(l-2):
        if s[i] != s[i+2]:    #移除兩個字串，看有沒有重複，沒有重複，則為新字串
            ans+=1

    print(ans)