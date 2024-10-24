from sys import stdin

def Input():
    return stdin.readline().rstrip()

ANS = list(map(int,Input().split()))
for _ in range(int(Input())):
    Gs = list(map(int,Input().split()))
    temp = ANS.copy()
    A = 0
    B = 0
    for i in range(4):
        if(temp[i] == Gs[i]):
            A += 1
            temp[i] = Gs[i] = None
    
    for i in range(4):
        if(temp.count(Gs[i]) and Gs[i] != None  ):
            B += 1
            temp[temp.index(Gs[i])] = Gs[i] = None

    print(A, 'A', B, 'B', sep='')