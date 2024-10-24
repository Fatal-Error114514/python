while True:
    try:
        x = int(input())
        y = int(input())
        m = int(input())
        print(pow(x, y, m))
        nothing = input()
    except:
        break