from itertools import permutations, starmap


ss = list(input())

def f(i, j):
    ss_prime = ss[:]
    ss_prime.insert(i, '3')
    ss_prime.insert(j, '5')
    return int(''.join(ss_prime)) % 21 == 0

print(int(any(starmap(f, permutations(range(len(ss)), 2)))))
