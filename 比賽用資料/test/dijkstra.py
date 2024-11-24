from math import inf

def dijkstra(graph, start):
    visited = []
    index = start
    node = dict((i, inf) for i in graph)
    node[start] = 0
    while len(visited) < len(graph):
        visited.append(index)
        for i in graph[index]:
            new_cost = node[index] + graph[index][i]
            if new_cost < node[i]:
                node[i] = new_cost
    
        next = inf
        for n in node:
            if n in visited:
                continue
            if node[n] < next:
                next = node[n]
                index = n
    return node

graph = {'A':{'A':0, 'B':2, 'C':4},
         'B':{'B':0, 'C':7, 'E':6},
         'C':{'C':0, 'D':6, 'E':2},
         'D':{'D':0, 'E':8, 'G':4},
         'E':{'E':0, 'G':2},
         'G':{'G':0}
        }
r = dijkstra(graph, 'A')
print(r)