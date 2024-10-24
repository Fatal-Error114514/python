for _ in range(int(input())):
    n = input()
    score = 0
    combo = 1
    for i in n:
        if i == 'O':
            score += combo
            combo += 1
        else:
            combo = 1
    print(score)