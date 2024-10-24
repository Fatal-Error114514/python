while True:
    try:
        lst = list(map(int,input().split()))
        table = []
        for i in lst:
            if(table):
                if(i > table[-1]):
                    table.append(i)
                else:
                    for j in range(len(table)):
                        if(table[j] > i):
                            table[j] = i
                            break
            else:
                table.append(i)
        print(len(table))
    except EOFError:
        break