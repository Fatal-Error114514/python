# https://zerojudge.tw/ShowProblem?problemid=a671

while True:
    try:
        a = int(input())
        b = int(input())
        print(round(pow(b, 1/a)))
    except EOFError:
        break
