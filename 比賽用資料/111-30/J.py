from bisect import bisect_left, bisect_right

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(n + 1) if is_prime[x]]

# def prime(a, b):
#     limit = int(b ** 0.5) + 1
#     primes = sieve(limit)

#     is_prime = [True] * (b - a + 1)

#     if a == 1:
#         is_prime[0] = False
    
#     for p in primes:
#         start = max(p * p, (a + p - 1) // p * p)
#         for j in range(start, b + 1, p):
#             is_prime[j - a] = False

#     return [i for i in range(a, b + 1) if is_prime[i - a]]

for _ in range(int(input())):
    a, b = map(int, input().split())
    p = sieve(int(b))
    print('\n'.join(map(str, p[bisect_left(p, a):bisect_right(p, b + 1)])))
    print()