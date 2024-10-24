import itertools

data = []

for i in range(5):
  n = int(input())
  data.append(n)


max = float('-inf')            #設定最小值為 負無限大
for v in itertools.permutations(data, 3):       #對data進行排列組合
  sum = 1
  for i in v:       #將i代入data的各種排列組合、進行乘積
    sum *= i

  if sum>max:       #若清單v的某種排列組合的三個乘積最大，則設定最大值
    max = sum
    a = list(v)

a.sort()
print("由%d,%d,%d相乘" % (a[0],a[1],a[2]))
print("最大乘積為%d" % max)