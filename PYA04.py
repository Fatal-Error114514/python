goal = int(input())
coin = list(map(int,input().split()))
for i in sorted(coin, reverse = True):
    count = 0
    while goal % i == 0:
        goal //= i
        count += 1
    if count != 0: print(f'${i}*{count}',end = '')