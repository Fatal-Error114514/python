from collections import Counter

n = input()
lst = Counter(input().split())
max_count = max(lst.values())
for k, v in sorted(lst.items()):
    if v == max_count:
        print(k, v)