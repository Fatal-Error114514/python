def f(x):
    if x == 1:
        return 1
    else:
        return (x - 1) + f(x - 1)

try:
    while True:
        print(f(int(input())))
except EOFError:
    pass