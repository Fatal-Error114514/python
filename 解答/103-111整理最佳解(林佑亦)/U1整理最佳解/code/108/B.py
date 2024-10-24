from sys import stdin

def Input():
    return stdin.readline().strip()

def check(n):
    if(lst[n].isdigit()):
        return int(lst[n])
    if(lst[n] == '/'):
        return 10 - int(lst[n-1])
    if(lst[n] == 'X'):
        return 10

for _ in range(int(Input())):
    lst = Input().split()
    score = 0
    round = 10
    p = 0
    while(round):
        if(lst[p].isdigit()):
            score += int(lst[p])
        elif(lst[p] == '/'):
            score += 10 - int(lst[p-1]) + check(p+1)
        else: # lst[p] == 'X'
            score += 10 + check(p+1) + check(p+2)
            round -= 0.5
        round -= 0.5
        p += 1
    print(score)
