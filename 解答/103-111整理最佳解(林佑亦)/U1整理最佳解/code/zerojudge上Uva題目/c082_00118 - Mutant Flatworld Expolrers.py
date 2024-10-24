# https://zerojudge.tw/ShowProblem?problemid=c082
drop = []
def change():
    global face
    if face == 1:
            face = 'N'
    elif face == 2:
        face = 'E'
    elif face == 3:
        face = 'S'
    elif face == 4:
        face = 'W'
land = input().split()
while True:
    try:
        lost = 0
        action = []
        x,y,face = input().split()
        x = int(x)
        y = int(y)
        action = input()
        for act in action:
            if face == 'N':
                face = 1
            elif face == 'E':
                face = 2
            elif face == 'S':
                face = 3
            elif face == 'W':
                face = 4
            if act == 'R':
                face += 1
            elif act == 'L':
                face -= 1
            elif act == 'F':
                last = [x,y]
                if face == 1:
                    y += 1
                elif face == 2:
                    x += 1
                elif face == 3:
                    y -= 1
                elif face == 4:
                    x -= 1
                for i in range(len(drop)):
                    if last == drop[i]:
                        if not(0<=x<=int(land[0]) and 0<=y<=int(land[1])):
                            x = last[0]
                            y = last[1]
                if not(0<=x<=int(land[0]) and 0<=y<=int(land[1])):
                    lost = 1
                    drop.append(last)
                    change()
                    print(*last,face,'LOST')
                    break
            if face == 5:
                face = 1
            elif face == 0:
                face = 4
        if(lost == 0):
            change()
            print(x,y,face)
    except EOFError:
        break