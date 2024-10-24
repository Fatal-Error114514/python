for _ in range(int(input())):
    n = list(input())
    output = ''
    while n:
        w = n.pop(0)
        x = ''
        while(len(n) and n[0].isdigit()):
            x += n.pop(0)
        output += w *int(x)
    print(output)
