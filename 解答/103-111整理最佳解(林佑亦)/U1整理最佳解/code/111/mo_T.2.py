from sys import stdin

def Input():
    return stdin.readline().rstrip()

def Do(p, path):
    isleaf = True
    path = path + [tree[p]]
    if(p*2 < len(tree) and tree[p*2] != 'null'): # 有左子樹
        Do(p*2, path)
        isleaf = False
    if(p*2+1 < len(tree) and tree[p*2 +1] != 'null'): # 有右子樹
        Do(p*2 +1, path)
        isleaf = False
    if(isleaf):
        print(*path, sep='->')

output = []
tree = [''] + Input().split(',')
Do(1, []) # 因為已經是二元樹的list了，所以直接走就好了

