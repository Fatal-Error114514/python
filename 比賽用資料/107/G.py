def diameter(n):
    if n >= len(tree) or tree[n] is None:
        return -1
    Ldiameter = diameter(n * 2 + 1)
    Rdiameter = diameter(n * 2 + 2)
    return max(height(n)[1] + height(n)[2] + 2, Ldiameter, Rdiameter)

def height(n):
    if n >= len(tree) or tree[n] is None:
        return -1, -1, -1
    Lheight, _, _ = height(n * 2 + 1)
    Rheight, _, _ = height(n * 2 + 2)
    return max(Lheight, Rheight) + 1, Lheight, Rheight

for _ in range(int(input())):
    tree = eval(input(), {'null': None})
    print(diameter(0))