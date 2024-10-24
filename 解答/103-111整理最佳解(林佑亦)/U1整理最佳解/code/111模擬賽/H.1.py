from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(Input())
    lst = [[0 for j in range(n)] for i in range(n)]
    num = 1
    queue = [[0, 0]]
    while(len(queue)):
        x,y = queue.pop(0)
        if(lst[x][y] == 0):
            lst[x][y] = num
            queue.append([x+1, y])
            queue.append([x, y+1])
            num += 1
        if([x, y] == [0, n-1]): 
            l = len(str(lst[x][y]))  
            break

    for i in range(n):
        for j in range(n):
            if(lst[i][j]):
                lst[i][j] = str(lst[i][j]).zfill(l)
            else:
                lst[i][j] = ''
    
    for i in lst:
        print(*i, sep='  ')

