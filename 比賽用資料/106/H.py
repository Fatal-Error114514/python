for _ in range(int(input())):
    num = input().split()
    p = 0
    while len(num) > 1:
        while num[p][-1].isdigit():
            p += 1
        num[p] = str(int(eval(num[p - 2] + num[p] + num[p - 1])))
        del num[p - 1]
        del num[p - 2]
        p -= 2
    print(num[0])