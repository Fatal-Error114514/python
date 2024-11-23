from itertools import permutations

s = list(input())
lst = []
for i in list(permutations(s)):
    i = list(i)
    if int(''.join(i)) not in lst and i != s:
        lst.append(int(''.join(i)))
for i in sorted(lst, reverse = True):
    print(i)