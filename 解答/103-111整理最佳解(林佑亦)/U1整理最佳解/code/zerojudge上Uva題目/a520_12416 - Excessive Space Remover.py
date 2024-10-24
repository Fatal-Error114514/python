# https://zerojudge.tw/ShowProblem?problemid=a520
while True:
    try:
        text = input()
        count = 0
        while(text.count('  ')):
            text = text.replace('  ', ' ')
            count += 1
        print(count)
    except EOFError:
        break
