def postorder(inorder, pre):
    root = pre.pop(0)
    i = inorder.index(root)
    l, r = inorder[:i], inorder[i + 1:]
    if len(l) > 1:
        l = postorder(l, pre)
    elif len(l):
        pre.remove(l[0])
    if len(r) > 1:
        r = postorder(r, pre)
    elif len(r):
        pre.remove(r[0])
    return l + r + [root]

for _ in range(int(input())):
    inorder = list(map(int,input().split(',')))
    preorder = list(map(int,input().split(',')))
    print(*postorder(inorder, preorder), sep = ',')