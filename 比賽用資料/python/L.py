from bisect import insort


xs = []
for n in range(1, int(input()) + 1):
    insort(xs, int(input()))

    if n % 2:
        print(xs[n // 2])
    else:
        print((xs[n // 2 - 1] + xs[n // 2]) // 2)

