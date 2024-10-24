def run_tree(i, path = []):
    is_leaf = True
    path.append(tree[i])
    if i * 2 + 1 < len(tree) and tree[i * 2 + 1] != 'null':
        run_tree(i * 2 + 1, path)
        is_leaf = False
    if i * 2 + 2 < len(tree) and tree[i * 2 + 2] != 'null':
        run_tree(i * 2 + 2, path)
        is_leaf = False
    if is_leaf:
        print(*path, sep = '->')
    path.pop()
tree = list(input().split(','))
run_tree(0)