from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = eval(Input())
    lst.sort()
    table = []
    for x,y in lst: #最常遞增子序列的方法
        if(table):
            for i,n in enumerate(table):
                if(n > y):
                    table[i] = y
                    break
            else:
                table.append(y)
        else:
            table.append(y)
    print(len(table))
