from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = Input()
dic = {}
while n:
    a,b = n.split()
    dic[b] = a
    n = Input()

n = Input()
while n:
    if(n in dic):
        print(dic[n])
    else:
        print('eh')
    n = Input()

