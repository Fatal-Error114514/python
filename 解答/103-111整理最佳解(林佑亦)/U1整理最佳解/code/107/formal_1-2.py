from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    lst = []
    winner = 3
    for i in range(3):
        n = list(Input())
        if(len(set(n)) == 1 and n[0] != '0'):
            winner = n[0]
        lst.append(n)
    if(winner == 3):
        for i in list(zip(*lst)):
            if(len(set(i)) == 1 and i[0] != '0'):
                winner = i[0]
                break
        else:
            if(lst[0][0] == lst[1][1] == lst[2][2] or lst[0][2] == lst[1][1] == lst[2][0]) and lst[1][1] != '0':
                winner = lst[1][1]
    print(winner)





