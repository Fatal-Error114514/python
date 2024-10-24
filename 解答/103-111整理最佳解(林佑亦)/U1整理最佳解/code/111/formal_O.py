# https://youtu.be/0JDMQVYexYE
n,goal = map(int,input().split())
coins = list(map(int,input().split()))
table = [0 for i in range(goal +1)]
table[0] = 1

for coin in coins:
    for i in range(coin, goal+1):
        table[i] = table[i] + table[i - coin]
print(table[-1])
