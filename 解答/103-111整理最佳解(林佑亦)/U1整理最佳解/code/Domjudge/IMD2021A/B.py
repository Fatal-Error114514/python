while True:
    try:
        a,b = map(int,input().split())
        if(a == b):
            print('Tie')
        elif(a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
            print('I won')
        else:
            print('I lost')
    except EOFError:
        break