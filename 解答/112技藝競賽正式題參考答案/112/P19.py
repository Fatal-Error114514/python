n = int(input())
ops = input()

for op in ops:
    if op == '+':
        n += 1
        s = str(n)
        n = int(s[-1] + s[:-1])
    else:
        n -= 1
        s = str(n)
        n = int(s[1:] + s[0])

print(n)
