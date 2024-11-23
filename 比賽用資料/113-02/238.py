from collections import Counter
s = Counter(input())
print(sorted(s.items(), reverse = True, key = lambda x: x[1])[0][0])