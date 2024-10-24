for _ in range(int(input())):
    n = list(input())
    if len(n) < 4:
        if sum(c1 == c2 for c1, c2 in zip(n, list('one'))) > sum(c1 == c2 for c1, c2 in zip(n, list('two'))):
            print(1)
        else:
            print(2)
    else:
        print(3)