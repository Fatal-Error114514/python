# https://zerojudge.tw/ShowProblem?problemid=a737

for _ in range(int(input())):
    lst = list(map(int,input().split()))
    del lst[0]
    lst = sorted(lst)
    p = (len(lst) -1) //2 
    p = lst[p]
    lst = [abs(i-p) for i in lst]
    print(sum(lst))






