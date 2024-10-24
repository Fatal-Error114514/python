from itertools import combinations, product
from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = int(Input())
ans = list(map(int,Input().split(',')))
for _ in range(n):
    guess = (list(map(int,Input().split(','))))
    bingo = list(set(ans) & set(guess))
    loss = list(set(guess) - set(bingo))
    output = []
    for i in range(2, 6):
        temp = []
        if(len(bingo) >= i) and (len(loss) >= 5-i):
            bp = list(list(j) for j in combinations(bingo, i))
            lp = list(list(j) for j in combinations(loss, 5-i))
            for j in product(bp, lp):
                temp.append(list(str(list(j)).replace('[', '').replace(']','').split(',')))
        output.append(len(temp))
    print(*output,sep=',')