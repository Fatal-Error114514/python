from collections import Counter

import re


s = input().lower()
counter = Counter(s)
vowel_count = sum(map(counter.__getitem__, 'aiueo'))

if vowel_count == 0:
    print(s)
elif vowel_count == 1:
    a, b, c = re.fullmatch(r'(\w*?)([aiueo])(\w*)', s).groups()
    print(a + b.upper() + c)
else:
    a, b, c, d, e = re.fullmatch(r'(\w*?)([aiueo])(\w*)([aiueo])(\w*?)', s).groups()
    print(a + b.upper() + c + d.upper() + e)

