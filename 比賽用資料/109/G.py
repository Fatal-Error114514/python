def dp(m, lst):
  table = [0 for i in range(m + 1)]
  for i in lst:
    for j in range(i, m + 1):
      table[j] = max(i + table[j - i], table[j - 1])
  return table[m]

while True:
  try:
    lst = list(map(int,input().split()))
    m, n = lst.pop(0), lst.pop(0)
    print(dp(m, lst))
  except EOFError:
    break