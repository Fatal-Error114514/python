for _ in range(int(input())):
    lst = eval(input())
    ind = sorted(lst)
    output = []
    while len(lst):
        i = 0
        temp = []
        while len(lst):
            a = ind.pop(i)
            b = lst.pop(i)
            temp.append(a)
            if a == b or b in temp:
                break
            i = ind.index(b)
        output.append(temp)
    print(output)