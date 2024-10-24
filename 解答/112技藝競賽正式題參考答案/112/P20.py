from collections import defaultdict


def get_prime_factors(k):
    factors = defaultdict(int)
    i = 2
    while i * i <= k:
        while k % i == 0:
            k //= i
            factors[i] += 1
        i += 1
    if k != 1:
        factors[k] += 1
    return factors


n = int(input())
prime_factors = get_prime_factors(n)

if 3 in prime_factors or 5 in prime_factors:
    print(0)
else:
    number_of_factors = 1
    for x in prime_factors.values():
        number_of_factors *= x + 1

    print(int(number_of_factors >= 5))
