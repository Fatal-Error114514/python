from sys import stdin

def Input():
    return stdin.readline().rstrip()

tree = [''] + Input().split(',')
output = []
visited = []
while(tree[1] != 'null'):
    i = 1
    temp = []
    while True:
        l = i*2
        r = i*2 +1
        temp.append(tree[i])
        if(l < len(tree)) and (tree[l] != 'null'):#有左子樹 and not null
            i = l
        elif(r < len(tree)) and (tree[r] != 'null'):#有右子樹 and not null
            i = r
        elif(tree[i] not in visited):
            output.append(temp)
            tree[i] = 'null'
            visited = list(set(visited + temp))
            break
        else:
            tree[i] = 'null'
            break
for i in output:
    print(*i,sep='->')
