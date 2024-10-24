from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    n = Input()
    visited = set()
    while(n != '1'):
        n = str(sum(list(map(lambda x:int(x)**2, n))))
        if(n in visited):
            print('F')
            break
        visited.add(n)
    else:
        print('T')
