n = eval(input())
data = []
time = [0]*1000

while n!=-1:
  data.append(n)
  time[data.index(n)] +=1
  n = eval(input())


num = time.count(max(time))

ans = []
for i in range(num):
  m = data[time.index(max(time))]
  ans.append(m)
  data.pop(time.index(max(time)))
  time.pop(time.index(max(time)))

ans.sort()

print(ans)