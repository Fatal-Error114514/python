n = int(input())
start = 2
s = 0
while n:
    for i in range(2, int(start**0.5) + 1):
        if start % i == 0:
            break
    else:
        s += start
        n -= 1
    start += 1
print(s)