from itertools import combinations
def eratosthenes(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]

Primelst = eratosthenes(100000) # 建表

n = int(input())
lst = list(map(int,input().split()))
for i in lst:
    insu = []
    num = [1]
    check = i
    for j in Primelst: # 找質因數
        if(j > i):
            break
        while(i % j == 0):
            i //= j
            num.append(j)
        
    
    for j in range(1, len(num)): # 做組合
        for k in combinations(num, j):
            x = 1
            for l in k:
                x *= l
            insu.append(x)
    insu = list(set(insu))
    if(check in insu):
        insu.remove(check)
    num = sum(insu)
    if(num == check):
        print('perfect')
    elif(num > check):
        print('abundant')
    else:
        print('deficient')
