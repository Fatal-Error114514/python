from collections import Counter


counter = Counter(input())
print(min([*map(counter.__getitem__, ['T', 'a', 'p', 'e']), counter['i'] // 2]))
