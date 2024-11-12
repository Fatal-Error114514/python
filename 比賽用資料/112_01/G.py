def f(x):
    if x == 1:
        return 1
    return x ** 2 + f(x - 1)


for i in iter(input,'0'):
    n = int(i)
    print(f(n))