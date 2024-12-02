def postorder(lst, path):
    if lst == []: return
    postorder([x for x in lst if x < lst[0]], path) # left child
    postorder([x for x in lst if x > lst[0]], path) # right child
    path.append(lst[0])
    return path

for _ in range(int(input())):
    n = int(input())
    lst = list(eval(input()))
    print(*postorder(lst, []), sep = ',')