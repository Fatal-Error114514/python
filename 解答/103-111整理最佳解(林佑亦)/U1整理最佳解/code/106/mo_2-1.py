from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = list(Input())
    x = lst.pop(0)
    if(x < 'I'):
        x = list(str(ord(x) - 55))
    elif(x == 'I'):
        x = ['3', '4']
    elif(x < 'O'):
        x = list(str(ord(x) - 56))
    elif(x == 'O'):
        x = ['3', '5']
    elif(x < 'W'):
        x = list(str(ord(x) - 57))
    elif(x == 'W'):
        x = ['3', '2']
    else:
        x = list(map(int,list(str(ord(x) - 58))))
    lst = list(map(int,(x + lst)))
    
    power = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    total = 0
    for i in range(len(power)):
        total += power[i] * lst[i]
    if(total % 10 == 0):
        print('T')
    else:
        print('F')