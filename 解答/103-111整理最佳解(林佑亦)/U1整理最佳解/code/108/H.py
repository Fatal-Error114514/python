from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a = int(Input())
    b = int(Input())
    lst = []
    for i in range(a):
        lst.append(list(map(int,Input().split())))
    table = [[float('inf') for j in range(b)] for i in range(a)]

    for i in range(a):
        for j in range(b):
            temp = []
            if(i-1 >= 0):
                temp.append(table[i-1][j])
            if(j-1 >= 0):
                temp.append(table[i][j-1])
            if(not temp):
                temp = [0]
            table[i][j] = min(temp) + lst[i][j]
    print(table[-1][-1])
            





