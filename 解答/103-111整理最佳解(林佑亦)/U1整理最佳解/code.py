for x in range(int(input())):
    n = int(input())
    dic = ['' for i in range(n+1)]
    far = [0 for i in range(n+1)]
    for i in range(n):
        a,b = map(int,input().split())
        dic[a] = b

    ans = 0
    for i in range(1, n+1):
        visited = [0 for i in range(n+1)] # True 可拜訪
        p = i
        while True:
            visited[p] = 1
            if(far[p]):
                visited += [1]*far[p]
            if(not visited[dic[p]]):
                p = dic[p]
            else:
                break
        far[i] = sum(visited)
        ans = i if far[i] > far[ans] else ans
    print(f'Case {x+1}: {ans}')
