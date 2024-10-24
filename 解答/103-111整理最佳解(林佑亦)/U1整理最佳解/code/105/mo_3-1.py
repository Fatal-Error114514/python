from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    tree = [''] + list(map(int,Input().split(',')))
    flag = None
    for i in range(1, len(tree)):
        if(i*2 < len(tree)):
            if(flag == None):
                flag = tree[i] > tree[i*2]
            if((tree[i] > tree[i*2]) != flag):
                print('F')
                break
        if(i*2 +1 < len(tree)):
            if(flag == None):
                flag = tree[i] > tree[i*2 +1]
            if((tree[i] > tree[i*2 +1]) != flag):
                print('F')
                break
    else:
        print('T')

