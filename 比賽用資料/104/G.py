def postorder(i):
    if i >= len(lst) or lst[i] is None:
        return
    postorder(i * 2 + 1)
    postorder(i * 2 + 2)
    path.append(lst[i])
for _ in range(int(input())):
    input()
    lst = list(eval(input()))
    path = []
    postorder(0)
    print(*path, sep = ',')