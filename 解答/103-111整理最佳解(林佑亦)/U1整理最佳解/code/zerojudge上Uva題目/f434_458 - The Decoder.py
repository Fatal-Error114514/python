# https://zerojudge.tw/ShowProblem?problemid=f434
while True:
    try:
        n = input()
        for i in n:
            print(chr(ord(i)-7),end='')
        print()
    except EOFError:
        break