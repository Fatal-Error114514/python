for _ in range(int(input())):
    g = []
    win = 3
    for i in range(3):
        n = list(input())
        if len(set(n)) == 1 and n[0] != '0':
            win = n[0]
        g.append(n)
    if win == 3:
        for i in list(zip(*g)):
            if len(set(i)) == 1 and i[0] != '0':
                win = i[0]
                break
        else:
            if g[0][0] == g[1][1] == g[2][2] or g[0][2] == g[1][1] == g[2][0] and g[1][1] != '0':
                win = g[1][1]
    print(win)