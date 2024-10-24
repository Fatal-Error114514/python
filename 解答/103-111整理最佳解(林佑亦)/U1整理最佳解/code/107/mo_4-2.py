from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = Input().split()
    lst = list(map(lambda x:x.split(','), lst))
    lst.sort(key= lambda x:int(x[2]),reverse=True)
    dic = {}
    cost = 0
    while(len(lst)):
        a,b,num = lst.pop()
        if(a not in dic):   dic[a] = [a]
        if(b not in dic):   dic[b] = [b]
        if(b not in dic[a]):
            for i in dic[b]:
                dic[a].append(i)
                dic[i] = dic[a] #故意指同一個記憶體
            cost += int(num)
    print(cost)
