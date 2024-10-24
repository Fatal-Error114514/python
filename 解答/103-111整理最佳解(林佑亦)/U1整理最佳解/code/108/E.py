from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b = map(int,Input().split())
    lst = []
    for i in range(a):
        lst.append(list(Input()))
    
    lst = list(zip(*lst))
    output = []
    DNA = ['A', 'C', 'G', 'T']
    
    for i in lst:
        x = 'Z'
        for j in DNA:
            if(i.count(j) > i.count(x)):
                x = j
        output.append(x)
    print(*output,sep='')
