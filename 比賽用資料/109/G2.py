from itertools import combinations

while True:
  try:
      items = list(map(int, input().split()))
      max_size = items.pop(0)
      del items[0]
      c = []
      for i in range(1, len(items) + 1):
         for j in combinations(items, i):
            if sum(j) <= max_size:
               c.append(sum(j))
      print(max(c))
  except EOFError:
      break