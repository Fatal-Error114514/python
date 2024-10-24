from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = Input()
    pw = len(n)
    total = sum(list(map(lambda x:int(x)**pw, list(n))))
    if(total == int(n)):
        print('Y')
    else:
        print('N')
