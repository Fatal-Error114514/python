def f(x):
    temp = []
    for i in range(0, len(x), 2):
        temp.append(str(3*int(x[i]) + int(x[i + 1])))
    return ''.join(temp)

p, q = input().split('.')
if len(p) % 2 != 0: p = '0' + p
if len(q) % 2 != 0: q += '0'
print(f(p), f(q), sep = '.')