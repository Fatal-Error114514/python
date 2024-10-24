from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    combo = 1
    lst = Input()
    score = 0
    for i in lst:
        if(i == 'O'):
            score += combo
            combo += 1
        else:
            combo = 1
    print(score)

