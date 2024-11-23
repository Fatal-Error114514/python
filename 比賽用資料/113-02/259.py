n = int(input())
lst = [n]
while n > 1:
    if n % 2 == 0:
        if n >= 4:
            n //= 4
        else:
            n //= 2
    else:
        n = n * 5 + 1
    lst.append(n)
print(*lst, sep = '->')