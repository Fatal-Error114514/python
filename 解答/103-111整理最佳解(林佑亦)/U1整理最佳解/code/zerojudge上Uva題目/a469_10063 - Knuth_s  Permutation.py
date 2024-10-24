# https://zerojudge.tw/ShowProblem?problemid=a469
n = input()
while n:
    n = list(n)
    lst = [n.pop(0)]
    for i in n:
        temp = []
        for j in range(len(lst)):
            for k in range(len(lst[j])+1):
                x = list(lst[j])
                x.insert(k, i)
                x = ''.join(x)
                temp.append(x)
        lst = temp.copy()

    for i in lst:
        print(*i, sep='')

    n = input()

'''
1.插入a
結果: a

2.插入b
結果: ba ab

3.插入c
結果: cba bca bac cab acb abc
'''