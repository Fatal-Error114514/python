from sys import stdin

def Input():
    return stdin.readline().rstrip()

dic = {
    'Y':{'Y':0,'O':2,'P':1},
    'O':{'Y':1,'O':0,'P':2},
    'P':{'Y':2,'O':1,'P':0}
}

for _ in range(int(Input())):
    a,b = Input().split(', ')
    print(dic[a][b])
