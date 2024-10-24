while True:
    try:
        n = input()
        for i in n:
            if(n.count(i) > 1):
                n = n.replace(i, '', n.count(i)-1)
        print(n)
    except EOFError:
        break