from itertools import permutations

n = input()
visited = set()
count = 0
for i in permutations(n):
    if int(''.join(i)) not in visited and int(''.join(i)) % 11 == 0:
        count += 1
        visited.add(int(''.join(i)))
print(count)