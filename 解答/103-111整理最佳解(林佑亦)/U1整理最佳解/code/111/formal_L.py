n = int(input())
count = 0
for i in range(1, n+1):
    i = bin(i)[2:]
    count += i.count('1')
print(count)