# https://zerojudge.tw/ShowProblem?problemid=a537

for p in range(1, int(input())+1):
    lst = input()
    print(f'Case {p}: ', end='')
    st = set(lst)
    output = []
    for i in st:
        x = lst.count(i)
        if(x == 1): continue
        for j in range(2, int(x**0.5)+1):
            if(x % j == 0):
                break
        else:
            output.append(i)
    
    if(output):
        print(*sorted(output),sep='')
    else:
        print('empty')

