from itertools import combinations, starmap


s = input()
if s.count('0') > 1:
    print(0)
else:
    def f(i, j):
        return int(s[:i] + s[i + 1:j] + s[j + 1:]) % 21 == 0
       
    print(int(any(starmap(f, combinations(range(len(s)), 2)))))
