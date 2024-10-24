def eratosthenes(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]

lst = eratosthenes(10**6)

n = int(input())
while n:
    count = 0
    for i in lst:
        if(i <= n and n % i == 0):
            count += 1
    print(f'{n} : {count}')
    n = int(input())
