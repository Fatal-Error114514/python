a, b = input().split(', ')
a = sum(int(a[-(i + 1)]) * 3 ** i for i in range(len(a)))
b = sum(int(b[-(i + 1)]) * 6 ** i for i in range(len(b)))
c = a + b
s = ''
while c > 0:
    s = str(c % 5) + s
    c//= 5
print(s)