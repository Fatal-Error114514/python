from collections import defaultdict
from math import inf

for _ in iter(input,'0 0 0'):
    case = 1
    graph = defaultdict(dict)
    node, line, problems = map(int,_.split())
    martix = [[0 for i in range(node)] for i in range(node)]

    for i in range(line):
        a, b, sound = map(int,input().split())
        martix[a - 1][b - 1] = sound
        martix[b - 1][a - 1] = sound
    
    for i in range(node):
        for j in range(node):
            if i != j and martix[i][j] == 0:
                martix[i][j] = inf
    
    for k in range(node):
        for i in range(node):
            for j in range(node):
                martix[i][j] = min(martix[i][j], martix[i][k] + martix[k][j])
    
    print(f'Case #{case}')
    for i in range(problems):
        start, end = map(int,input().split())