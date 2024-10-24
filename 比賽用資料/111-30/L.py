def bit(num):
    lst = []
    for i in range(1, num + 1):
        b = ''
        while i > 0:
            b = str(i % 2) + b
            i //= 2
        lst.append(b)
    return lst

count = 0
num = int(input())
for n in bit(num):
    for j in n:
        if j == '1':
            count += 1
print(count)