from collections import Counter
country = Counter()
for _ in range(int(input())):
    data = input()
    country[data.split()[0]] += 1
for i in sorted(country):
    print(i,country[i])