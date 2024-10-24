from sys import stdin
# python p41.py<in1.txt
while True:
    pt = int(stdin.readline())
    if pt == 0:
        break
    data = []
    x = 1
    dic = {}
    for i in range(pt):
        dic[i+1] = set()
    while True:
        x = stdin.readline().strip()
        if x == "0":
            break
        x = list(map(int,x.split()))
        for i in range(1,len(x)):
            dic[x[0]].add(x[i])
            dic[x[i]].add(x[0])
        data.append(x)
    for i in dic:
        dic[i] = list(dic[i])

    ans = []
    for i in range(1,pt+1):
        oppt = i+1
        if oppt>pt:oppt=1
        run = [oppt]
        visit = set()
        t = dic.copy()
        del t[i]
        while True:
            for j in dic[run[0]]:
                if j == i or j in visit:
                    continue
                run.append(j)
                visit.add(j)
            run.pop(0)
            if run == []:
                break
        if len(visit) != pt-1:
            ans.append(i)
    print(len(ans))