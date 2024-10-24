from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = list(map(int,Input().split(',')))
    dic = {}
    queue = lst.copy()
    while(len(queue) > 1):
        queue.sort()
        num = queue[0] + queue[1]
        dic[queue[0]] = num
        dic[queue[1]] = num
        queue[0] = num
        del queue[1]
    
    root = queue[0]

    output = []
    for i in lst:
        count = 0
        while(i != root):
            i = dic[i]
            count += 1
        output.append(count)
    print(*output,sep=',')

