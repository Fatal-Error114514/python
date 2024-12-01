from itertools import permutations

for _ in range(int(input())):
    i, j, k = eval(input())
    p = list(permutations(str(i)))
    j, k = int(''.join(p[j - 1])),int(''.join(p[k - 1]))
    print(j + k)