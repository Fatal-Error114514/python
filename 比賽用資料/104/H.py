for _ in range(int(input())):
    s = input().split()
    edges = []
    for i in s:
        node1, node2, c = i.split(',')
        edges.append((node1, node2, int(c)))
    edges.sort(key = lambda x: x[2])

    tree = {}
    for i in edges:
        tree[i[0]] = [i[0]]
        tree[i[1]] = [i[1]]
    cost = 0
    while len(edges) > 1:
        a = edges[0][0]
        b = edges[0][1]
        if b not in tree[a]:
            if len(tree[a]) == len(tree[b]) == 1:
                tree[a].append(b)
                tree[b] = tree[a]
            else:
                tree[a] += tree[b]
                for i in tree[b]:
                    tree[i] = tree[a]
            cost += edges[0][2]
        del edges[0]
    print(cost)