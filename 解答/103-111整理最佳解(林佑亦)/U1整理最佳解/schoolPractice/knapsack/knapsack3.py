def change(s):
    s = list(map(int,s.split()))

    n = s[0]
    del s[0]
    lst = [float('inf')]*(n+1)
    lst[0] = 0
    ans = ['']*(n+1)

    for i in s:
        for j in range(i,n+1):
            if(lst[j] > lst[j-i] + 1):
                lst[j] = lst[j-i] + 1
                ans[j] = ans[j-i] + ' ' + str(i)

    ans = list(map(int,ans[-1].split()))
    s.sort(reverse=1)
    for p in s:
        print('%d元:%d枚' %(p, ans.count(p)))

change("656 8 45 15 35 5 60 1")