from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = Input()
while n:
    lst = n + ' '
    while(not lst.count('()')):
        lst += Input() + ' '
    lst = lst.replace('(', '').replace(')', '').split()
    dic = {}
    for i in lst:
        num,lr = i.split(',')
        if(lr in dic):
            print('not complete')
            break
        dic[lr] = num
    else:
        if('' not in dic):
            print('not complete')
            n = Input()
            continue
        queue = ['']
        output = []
        while(queue): #BFS
            p = queue.pop(0)
            output.append(dic[p])
            if(p + 'L' in dic):
                queue.append(p + 'L')
            if(p + 'R' in dic):
                queue.append(p + 'R')
        if(len(output) == len(dic)): #確認有沒有都拜訪了，沒有代表中間有漏的
            print(*output)
        else:
            print('not complete')
    n = Input()