n = int(input())
a = [n]
while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    a.append(n)
print(*a)