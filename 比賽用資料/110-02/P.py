'''def dp(coin, count):
    lst = []
    for i in coin:
        for j in range(len(lst)):
            lst.append(lst[j] + i)
        lst.append(i)
    lst = set(sorted(lst))

    print(len(lst))
    print(*lst)'''
def dp(coin, count):
    lst = {0}
    for x in coin:
        lst |= {x + i for i in lst}
    lst.remove(0)
    print(len(lst))
    print(*sorted(lst))
count = int(input())
coin = list(map(int,input().split()))
dp(coin, count)